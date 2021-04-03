# -*- coding: iso-8859-1 -*-
""" tomarkdown.py

Converts IANA regions (countries) into a simple markdown file.

Author: Henrique Moreira, h@serrasqueiro.com
"""

# pylint: disable=missing-function-docstring

import sys
import os.path
import packreg.ianacountries as ianacountries

DEF_OUTPUT = "reference.md"
MY_ENCODING = "ISO-8859-1"
MY_OUT_ENCODING = MY_ENCODING


def main():
    runner(sys.argv[1:])

def runner(args):
    if args:
        if tuple(args) == (".",):
            outname = DEF_OUTPUT
        else:
            assert len(args) == 1, "At most one arg expected"
            outname = args[0]
    else:
        outname = ""
    adict = ianacountries.load_all()
    iana = adict["iana"]
    basics = [displayed_item_str(key, iana[key]) for key in sorted(iana)]
    if outname:
        dump_to_markdown(outname, [(key, displayed_item(iana[key])) for key in sorted(iana)])
    else:
        print('\n'.join(basics))


def dump_to_markdown(outname, tuplist, dump=True) -> str:
    file_short = os.path.basename(outname)
    if file_short.endswith((".md", ".markdown")):
        file_short = ''.join(file_short.split('.')[:-1])
    assert file_short, "Empty name?!"
    text = f"""# {file_short} (markdown file)

## Countries / Regions

"""
    names = dict()
    for abbrev, name in tuplist:
        assert name, "Empty country description!?"
        #print(abbrev, name)
        hint = " (no SVG!)"
        svg_name = f"svg/{abbrev}.svg"
        if os.path.isfile(svg_name):
            hint = ' [(svg here)](./{} "{}")'.format(
                svg_name,
                name,
                )
        linestr = f"- {abbrev} -- {name}{hint}\n"
        text += linestr
        names[name] = f"- {name} --{hint}\n"
    if dump:
        print(text)
    text += """
## Sorted by country name

"""
    for name in sorted(names):
        text += names[name]
    if not outname:
        return text
    with open(outname, "w", encoding=MY_OUT_ENCODING) as fout:
        fout.write(text)
    return text


def displayed_item(entry: dict) -> str:
    shown = ianacountries.strip_accents(entry['Description'])
    return shown

def displayed_item_str(key: str, entry: dict) -> str:
    shown = displayed_item(entry)
    astr = f"{key}: {shown}"
    return astr


if __name__ == '__main__':
    main()
