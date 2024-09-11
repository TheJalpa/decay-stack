import os
import sys
import re
import shutil
import argparse

# We are going to setup an argument on whether we want to apply terraform, or destroy it
# You can use this for various types of argument applications from passing variables
# To telling terraform how to handle workspaces, or whatever works for your use case.
parser = argparse.ArgumentParser()
parser.add_argument("--search", required=False, type=str)
args = parser.parse_args()
searchpattern = args.search

f = open('types.xml', "r")
copy = open("tradertypes.xml", "w")
for line in f:
    if re.match(r'^\s*$', line):
        pass
    elif re.match(r'[ \t]+<type name=', line):
        print("Found type : " + str(line))
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