import os
import sys
import re
import shutil
from dayzvars import *
f = open('modlist.txt', "r")
lines = f.read().splitlines()
for line in lines:
    #print(line)
    try:
        os.system('ln -s steamapps/workshop/content/221100/' + line + '/ ' + homedir + '/' + line)
    except:
        print('ln -s failed, likely due to already existing')
    try:
        os.system('cd ' + homedir + ' && cp ' + line + '/Keys/* keys/')
    except:
        print('Copying keys failed likely because of naming conventions, will try with keys instead of Keys')
    try:
        os.system('cd ' + homedir + ' && cp ' + line + '/keys/* keys/')
    except:
        print('Copying keys on second try failed, check file structure.')
    try:
        #because some people are annoying and deviate from naming conventions.
        os.system('cd ' + homedir + ' && cp ' + line + '/key/* keys/')
    except:
        print('Copying keys on second try failed, check file structure.')
    try:
        os.system('cd ' + homedir + ' && cp ' + line + '/Key/* keys/')
    except:
        print('Copying keys on second try failed, check file structure.')