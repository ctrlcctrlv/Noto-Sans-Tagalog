# $fontforge -lang=py -script WWQ.py

import fontforge as ff
import shutil

masters = ["Regular", "Bold"]
family = "NotoSansTagalog"
sfds = ["{}-{}.sfd".format(family, master) for master in masters]
ufos = ["{}-{}-FontForge.ufo".format(family, master) for master in masters]

for ufo in ufos:
    try:
        shutil.rmtree(ufo)
    except FileNotFoundError:
        continue

for i, sfd in enumerate(sfds):
    f = ff.open(sfd)
    f.generate(ufos[i], flags=("no-hints", "omit-instructions"))
    f.close()
