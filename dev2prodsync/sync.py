import argparse
import os
from dzvars import *
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--dzbranch", required=True, type=str)
parser.add_argument("--dzrun", required=True, type=str)
args = parser.parse_args()
dzbranch = args.dzbranch
dzrun = args.dzrun

def run_rsync(source, destination, options=None):
    command = ['rsync']
    if options:
        command.extend(options)
    command.extend([source, destination])

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print("rsync completed successfully.")
        return True
    else:
        print("rsync failed with error:")
        print(result.stderr)
        return False

if dzrun == "true":
    rsync_options = ['-av', '--dry-run']
    if dzbranch == "dev":    
        run_rsync(clonedir + "profiles/", devprofiledir, rsync_options)
        run_rsync(clonedir + "profiles/", devmaploc, rsync_options)
    if dzbranch == "prod":
        run_rsync(clonedir + "profiles/", prodprofiledir, rsync_options)
        run_rsync(clonedir + "profiles/", prodmaploc, rsync_options)
    else:
        print("No correct branch specified.")
if dzrun == "false":
    rsync_options = ['-av']
    if dzbranch == "dev":    
        run_rsync(clonedir + "profiles/", devprofiledir, rsync_options)
        run_rsync(clonedir + "profiles/", devmaploc, rsync_options)
    if dzbranch == "prod":
        run_rsync(clonedir + "profiles/", prodprofiledir, rsync_options)
        run_rsync(clonedir + "profiles/", prodmaploc, rsync_options)
    else:
        print("No correct branch specified.")