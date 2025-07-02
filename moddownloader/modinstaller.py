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
f = open(vars.clonedir + '/' + branch_modules[branch] + '/modlist.txt', "r")
lines = f.read().splitlines()
for line in lines:
    #print(line)
    try:
        os.system('ln -s steamapps/workshop/content/221100/' + line + '/ ' + vars.homedir + '/' + line)
    except:
        print('ln -s failed, likely due to already existing')
    try:
        os.system('cd ' + vars.homedir + ' && cp ' + line + '/Keys/* keys/')
    except:
        print('Copying keys failed likely because of naming conventions, will try with keys instead of Keys')
    try:
        os.system('cd ' + vars.homedir + ' && cp ' + line + '/keys/* keys/')
    except:
        print('Copying keys on second try failed, check file structure.')
    try:
        #because some people are annoying and deviate from naming conventions.
        os.system('cd ' + vars.homedir + ' && cp ' + line + '/key/* keys/')
    except:
        print('Copying keys on second try failed, check file structure.')
    try:
        os.system('cd ' + vars.homedir + ' && cp ' + line + '/Key/* keys/')
    except:
        print('Copying keys on second try failed, check file structure.')