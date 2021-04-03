#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-
""" ianacountries.py

Shows IANA regions;
inspired on regions.py -- see `https://github.com/behdad/region-flags/blob/gh-pages/regions.py`

Author: Henrique Moreira, h@serrasqueiro.com
"""

# pylint: disable=missing-function-docstring, invalid-name, line-too-long

import unicodedata

LANG_SUBTAG_REG = "data/language-subtag-registry"
LANG_SUBTAG_PRIV = "data/language-subtag-private"


def main():
    load_all(True)


def load_all(dump: bool=False) -> dict:
    text_list = list()
    filenames = (
        LANG_SUBTAG_REG,
        LANG_SUBTAG_PRIV,
        )
    regions = load_regions(filenames)
    for akey in sorted(regions):
        entry = regions[akey]
        infos = (
            strip_accents(entry['Description']),
            [(item, aval) for item, aval in entry.items() if item != 'Description'],
            )
        shown = f"{infos[0]} = {infos[1]}"
        text_list.append(shown)
        if dump:
            print('%s%s%s' % (akey, "\t", shown))
    result = {
        "iana": regions,
        "info": text_list,
        }
    return result


def load_regions(filenames) -> dict:
    assert isinstance(filenames, (tuple, list)), "filenames should be either a list (or tuple)"
    entries = []
    for filename in filenames:
        entries.extend(load_region_entries(filename))
    regions = {
        e['Subtag']: e
        for e in entries
        if e['Type'] == 'region'
        and len(e['Subtag']) == 2
        and e['Description'] != 'Private use'
        and 'Deprecated' not in e
    }
    for r_val_key in regions.values():
        del r_val_key['Type']
        del r_val_key['Subtag']
    return regions


def load_region_entries(filename):
    entries = []
    entry = {}
    fields = []

    region_file_obj = open(filename, encoding='utf-8')
    region_file_obj.readline()
    region_file_obj.readline()

    for line in region_file_obj:
        if line.startswith('%%'):
            entries.append(entry)
            entry = {}
            continue
        if line.startswith('  '):
            # Continuation
            entry[fields[0]] += ' ' + line.strip()
            continue
        fields = [x.strip() for x in line.split(':')]
        entry[fields[0]] = fields[1]
    entries.append(entry)
    return entries


def strip_accents(s):
    """ Replaces accents by an ASCII equivalent character
    (not a Latin-1 accent, for instance)
    """
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


if __name__ == '__main__':
    main()
