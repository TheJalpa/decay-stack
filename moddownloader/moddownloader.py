import os
import sys
import re
import shutil
from dayzvars import *

if os.path.exists("dayzmods.sh"):
    os.remove("dayzmods.sh")
os.system('touch dayzmods.sh')
if os.path.exists("moddump.txt"):
    os.remove("moddump.txt")
os.system('touch moddump.txt')

f = open('modlist.txt', "r")
copy = open("dayzmods.sh", "w")
steamworkshop = ''
for line in f:
    steamworkshop = steamworkshop + '+workshop_download_item 221100 ' + line
moddump = open("moddump.txt", "a")
moddump.write(steamworkshop)
moddump.close()
moddump = open("moddump.txt", "r")
lines = moddump.readlines()
mystr = ' '.join([line.strip() for line in lines])
print(mystr)
copy.write('cd ' + steamcmdhomedir + '\n')
copy.write('./steamcmd.sh +force_install_dir ' + homedir + ' +login ' + steamlogin + ' ' + steampass + ' ' + mystr + ' +quit')
f.close()
copy.close()
#os.system('cd ' + homedir)
os.remove("moddump.txt")

f = open('manualmods.txt', "r")
copy = open("manualdump.txt", "w")
steamworkshop = ''
for line in f:
    steamworkshop = steamworkshop + '' + line + ';'
moddump = open("manualdump.txt", "a")
moddump.write(steamworkshop)
moddump.close()
moddump = open("manualdump.txt", "r")
lines = moddump.readlines()
manualstr = ''.join([line.strip() for line in lines])
print(manualstr)

f = open('modlist.txt', "r")
copy = open("startdayz.sh", "w")
steamworkshop = ''
for line in f:
    steamworkshop = steamworkshop + '' + line + ';'
moddump = open("moddump.txt", "a")
moddump.write(steamworkshop)
moddump.close()
moddump = open("moddump.txt", "r")
lines = moddump.readlines()
mystr = ''.join([line.strip() for line in lines])
manualstr = manualstr[:-1]
copy.write('!#/bin/bash\n')
copy.write('./DayZServer -config=serverDZ.cfg -profile=profiles \'-mod=' + mystr + manualstr + '\' -dologs -adminlog -netlog -freezecheck -BEpath=battleeye')
f.close()
copy.close()
#os.system('cd ' + homedir)
os.remove("moddump.txt")
os.remove("manualdump.txt")