# patching -- [region-flags](https://github.com/serrasqueiro/region-flags)

You can download the reduced repository by cloning only one branch, called `mydev` (actually 'new/mydev'):
- `git clone -b new/mydev --single-branch git@github.com:serrasqueiro/region-flags.git`

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

In case you have dangling branches on your local workspace with e.g. '.../remotes/origin/...', such as the ones that are shown by `git branch -a | grep /origin/`:
```
remotes/origin/HEAD -> origin/master
remotes/origin/gh-pages
remotes/origin/master
remotes/origin/new/mydev
remotes/origin/new/parot
```
you can get rid of the ones that have no equivalent on github; just do:
- `git remote prune origin`

