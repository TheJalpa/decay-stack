import os
import sys
import re
import shutil
import argparse
import platform

f = open('types.xml', "r")
copy = open("tradertypes.xml", "w")
for line in f:
    if re.match(r'^\s*$', line):
        pass
    elif re.match(r'[ \t]+<type name=', line):
        #print("Found type : " + str(line))
        type1 = "<type name=\""
        type2 = "\">"
        pattern1 = line.index(type1)
        pattern2 = line.index(type2)         
        res = ''
        for indexing in range(pattern1 + len(type1), pattern2):
            res = res + line[indexing]
        copy.write(res+'\n')
    else:
        pass
copy.write('\n')
f.close()
copy.close()

#Shoutout to https://github.com/tknorris23 for this
#This will diff the files and give you a list of all of these
#The end result is to output sorted.txt which is a list of all missing trader items, alphabetically

item_list = set()
items = open('tradertypes.xml', 'r', encoding="utf-8")

for line in items:
    item_list.add(line.strip())
    
items.close()

file = open('TraderConfig.txt', 'r', encoding="utf-8")

for line in file:
    text = line.split(',', 1)[0].strip()
    if text in item_list:
        item_list.discard(text)
file.close()

writer = open('output.txt', 'w', encoding="utf-8")

for item in item_list:
    writer.write(item + '\n')

writer.close()
if platform.system() == "Windows":
    print("")
else:
    print('Sorting types into sorted.txt')
    os.system('more output.txt | sort -n > sorted.txt && rm output.txt')