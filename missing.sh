#!/usr/bin/env sh

./regions.py | while read x y; do test -f "png/$x.png" || echo $x $y; done

# Now let's re-generate 'reference.md'
export PYTHONPATH=$PYTHONPATH:src

python3 src/packreg/tomarkdown.py .

