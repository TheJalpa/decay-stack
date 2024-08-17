import os
import sys
import re
import shutil

if os.path.exists("types.xml"):
    os.remove("types.xml")
os.system('touch types.xml')

f = open('originalxml/types.xml', "r")
copy = open("types.xml", "w")
for line in f:
    if re.match(r'^\s*$', line):
        print('Empty line found, skipping')
    elif re.match(r'</types>', line):
        print('Found </types>, skipping')
        print(line)
    else:
        copy.write(line)
copy.write('\n')
f.close()
copy.close()

listfiles = os.listdir('modsxml')
print(listfiles)
for xmls in listfiles:
    modlink = "modsxml/" + xmls
    f = open(modlink, "r")
    copy = open("types.xml", "a")
    for line in f:
        if re.match(r'^\s*$', line):
            print('Empty line found, skipping')
        elif re.match(r'<\?xml version', line):
            print('removing headliner')
        elif re.match(r'<types>', line):
            print('Found <types>, skipping')
            print(line)
        elif re.match(r'</types>', line):
            print('removing trailing </types>, skipping')
        else:
            copy.write(line)
    f.close()
copy.write('</types>')
copy.close()