#!/bin/bash

FONTFORGE=/home/osboxes/Workspace/fontforge/build/bin/fontforge
if test -z $DEBUG; then DEBUG='INFO'; fi

if test -e $FONTFORGE; then
    true
else
    FONTFORGE=`which fontforge`
fi

$FONTFORGE -lang=py -script build.py

for f in *FontForge.ufo; do
    rm -r ${f/-FontForge/} || true
    cp -r "$f" ${f/-FontForge/}
    (cat ${f/-FontForge/}/features.fea; cat features.fea) > ${f/-FontForge/}/features.fea.tmp
    mv ${f/-FontForge/}/features.fea.tmp ${f/-FontForge/}/features.fea
done

fontmake --verbose $DEBUG -m NotoSansTagalog.designspace -o variable --keep-overlaps --optimize-cff 0 --no-optimize-gvar --keep-direction --output-path NotoSansTagalog[wght].ttf
ttfautohint -s NotoSansTagalog[wght].ttf NotoSansTagalog-hinted.ttf
rm dist/*
mv NotoSansTagalog-hinted.ttf dist/NotoSansTagalog[wght].ttf

fontmake --verbose $DEBUG -m NotoSansTagalog.designspace -o ttf -i --keep-overlaps --optimize-cff 0 --keep-direction
mv instance_ttf/*.ttf dist
rmdir instance_ttf

for f in dist/*.ttf; do
    gftools fix-dsig --autofix "$f"
done
