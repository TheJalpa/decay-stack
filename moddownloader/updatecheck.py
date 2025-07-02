import requests
from bs4 import BeautifulSoup
import os
import importlib
import sys
import time
from datetime import datetime

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
if branch in branch_modules:
    vars = importlib.import_module(branch_modules[branch])
    print(f"Loaded variables from {branch_modules[branch]}")
else:
    print(f"Error: Unknown branch '{branch}'")
    sys.exit(1)
#f = open(vars.clonedir + '/' + branch_modules[branch] + '/modlist.txt', "r")
MOD_ID_FILE = vars.clonedir + '/' + branch_modules[branch] + '/modlist.txt'
MOD_UPDATE_FILE = vars.clonedir + '/' + branch_modules[branch] + "/mod_updates.csv"
def get_workshop_mod_update_time(mod_id):
    url = f"https://steamcommunity.com/sharedfiles/filedetails/?id={mod_id}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"[{mod_id}] Failed to fetch page: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    labels = soup.find_all("div", class_="detailsStatLeft")
    values = soup.find_all("div", class_="detailsStatRight")

    for label, value in zip(labels, values):
        if "Updated" in label.text:
            return value.text.strip()

    print(f"[{mod_id}] Could not find update time on page")
    return None

def load_mod_ids(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def load_stored_updates(filename):
    updates = {}
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",", 1)
                if len(parts) == 2:
                    updates[parts[0].strip()] = parts[1].strip()
    return updates

def save_updates_to_csv(updates, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for mod_id, update_time in sorted(updates.items()):
            f.write(f"{mod_id},{update_time}\n")

def main():
    mod_ids = load_mod_ids(MOD_ID_FILE)
    stored_updates = load_stored_updates(MOD_UPDATE_FILE)
    updated_any = False

    for mod_id in mod_ids:
        current_time = get_workshop_mod_update_time(mod_id)
        if not current_time:
            continue  # Skip on error

        stored_time = stored_updates.get(mod_id)

        if stored_time is None:
            print(f"[{mod_id}] New mod detected! Added to tracking.")
            stored_updates[mod_id] = current_time
            updated_any = True

        elif stored_time != current_time:
            print(f"[{mod_id}] Time to update! New time: {current_time}")
            os.system('bash ')
            stored_updates[mod_id] = current_time
            updated_any = True

        else:
            print(f"[{mod_id}] Up to date.")
        time.sleep(4)
    if updated_any:
        print('Updating and restarting')
        save_updates_to_csv(stored_updates, MOD_UPDATE_FILE)
        os.system('bash update' + branch_modules[branch] + '.sh && sudo systemctl restart dayz' + branch_modules[branch] + ' && echo updated mods at ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' >> updatelog.txt')
if __name__ == "__main__":
    main()
