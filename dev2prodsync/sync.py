import argparse
import os
from dzvars import *
import subprocess
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("--dzbranch", required=True, type=str)
parser.add_argument("--dzrun", required=True, type=str)
parser.add_argument("--dzmap", required=True, type=str)
args = parser.parse_args()
dzbranch = args.dzbranch
dzrun = args.dzrun
dzmap = args.dzmap
def devkeys():
    # Define the base directory (where this script is run)
    base_dir = devserverdir

    # Destination directory (./keys)
    dest_dir = os.path.join(base_dir, "keys")
    os.makedirs(dest_dir, exist_ok=True)

    # Valid subfolder names to look for
    key_folder_names = {"key", "keys", "Keys"}

    # Loop through folders in current directory
    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)
        
        # Only look at folders with '@' in the name
        if os.path.isdir(folder_path) and "@" in folder_name:
            # Look for "key"/"keys"/"Keys" subfolder inside
            for key_name in key_folder_names:
                potential_key_path = os.path.join(folder_path, key_name)
                if os.path.isdir(potential_key_path):
                    print(f"Found key folder in {folder_name}: {key_name}")
                    
                    # Copy each file in the key folder to ./keys/
                    for file_name in os.listdir(potential_key_path):
                        src_file = os.path.join(potential_key_path, file_name)
                        dest_file = os.path.join(dest_dir, file_name)

                        if os.path.isfile(src_file):
                            if not os.path.exists(dest_file):
                                shutil.copy2(src_file, dest_file)
                                print(f"  Copied {file_name} to ./keys/")
                            else:
                                print(f"  Skipped {file_name} (already exists)")
                    break  # Stop after finding the first valid key folder

    print("Done.")
#Vars used:
#clonedir = ""
#devprofiledir = ""
#devmaploc = ""
#prodprofiledir = ""
#prodmaploc = ""

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
        run_rsync(clonedir + "map/", devmaploc, rsync_options)
        exit('Successfuly finished')
    if dzbranch == "prod":
        run_rsync(clonedirprod + "profiles/", prodprofiledir, rsync_options)
        run_rsync(clonedirprod + "map/", prodmaploc, rsync_options)
        exit('Successfuly finished')
    else:
        print("No correct branch specified.")
if dzrun == "false":
    rsync_options = ['-av']
    if dzbranch == "dev":   
        if os.path.exists(dzmap):
            clonedir = clonedir + '/' + dzmap + '/'
            os.system('ls ' + clonedir) 
            os.system('ls ' + devprofiledir)
            run_rsync(clonedir + "profiles/", devprofiledir, rsync_options)
            run_rsync(clonedir + "map/", devmaploc, rsync_options)
            devkeys()
            exit('Successfuly finished')
        else:
            print('Exiting as you entered an invalid map config')
            exit(1)
    if dzbranch == "prod":
        if os.path.exists(dzmap):
            clonedir = clonedir + '/' + dzmap + '/'
            os.system('sudo chattr -i ' + prodprofiledir + "LBmaster/Config/LBBanking/ATMConfig.json")
            os.system('sudo chattr -i ' + prodprofiledir + "LBmaster/Config/LBBanking/ATMPositions.json")
            run_rsync(clonedirprod + "profiles/", prodprofiledir, rsync_options)
            run_rsync(clonedirprod + "map/", prodmaploc, rsync_options)
            os.system('sudo chattr +i ' + prodprofiledir + "LBmaster/Config/LBBanking/ATMConfig.json")
            os.system('sudo chattr +i ' + prodprofiledir + "LBmaster/Config/LBBanking/ATMPositions.json")
            exit('Successfuly finished')
        else:
            print('Exiting as you entered an invalid map config')
            exit(1)
    else:
        print("No correct branch specified.")