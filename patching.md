# patching -- [region-flags](https://github.com/serrasqueiro/region-flags)

Place yourself on the 'parot' branch, by doing:
- `git checkout new/parot`

Check whether upstream repository (where this repo was forked from) has any news:

```
git remote add --mirror=fetch upstream git@github.com:behdad/region-flags.git
git fetch upstream
git pull upstream gh-pages
git pull upstream --tags gh-pages
```

# the end
Unlike "The Doors" *The End*, this end shows what you might want to do from here on.

```
git remote remove upstream
git checkout master
git fetch --all
```
