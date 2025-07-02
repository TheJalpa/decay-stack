import os
import sys
import re
import shutil
import sys
import importlib

# Get the branch argument (assuming format: python3 script.py --branch xyz)
if "--branch" in sys.argv:
    branch_index = sys.argv.index("--branch") + 1
    if branch_index < len(sys.argv):
        branch = sys.argv[branch_index]
    else:
        print("Error: --branch needs a value.")
        sys.exit(1)
else:
    print("Error: Missing --branch argument.")
    sys.exit(1)

# Map branches to module names
branch_modules = {
    "deerisle": "deerisle",
    "melkar": "melkar",
}

# Import the right vars file
if branch in branch_modules:
    vars = importlib.import_module(branch_modules[branch])
    print(f"Loaded variables from {branch_modules[branch]}")
else:
    print(f"Error: Unknown branch '{branch}'")
    sys.exit(1)

if os.path.exists('dayzmods' + branch_modules[branch] + '.sh'):
    os.remove('dayzmods' + branch_modules[branch] + '.sh')
os.system('touch dayzmods' + branch_modules[branch] + '.sh')
if os.path.exists("moddump.txt"):
    os.remove("moddump.txt")
os.system('touch moddump.txt')

f = open('modlist.txt', "r")
copy = open('dayzmods' + branch_modules[branch] + '.sh', "w")
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
copy.write('cd ' + vars.steamcmdhomedir + '\n')
copy.write('./steamcmd.sh +force_install_dir ' + vars.homedir + ' +login ' + vars.steamlogin + ' ' + vars.steampass + ' ' + mystr + ' +quit')
f.close()
copy.close()
os.remove("moddump.txt")

f = open(vars.clonedir + '/' + branch_modules[branch] + '/manualmods.txt', "r")
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

f = open(vars.clonedir + '/' + branch_modules[branch] + '/modlist.txt', "r")
copy = open('startdayz' + branch_modules[branch] + '.sh', "w")
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
os.remove("moddump.txt")
os.remove("manualdump.txt")