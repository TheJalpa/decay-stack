import sys
import re
import importlib

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

branch_modules = {
    "deerisle": "deerisle",
    "melkart": "melkart",
}
if branch in branch_modules:
    vars = importlib.import_module(branch_modules[branch])
    print(f"Loaded variables from {branch_modules[branch]}")
else:
    print(f"Error: Unknown branch '{branch}'")
    sys.exit(1)

file_path = "../" + branch_modules[branch] + '/profiles/Trader/TraderConfig.txt'

with open(file_path, "r") as f:
    raw_lines = [line.rstrip("\n") for line in f]

cleaned_lines = []

for line in raw_lines:
    # Leave lines with <...> or comments or empty lines untouched
    if ("<" in line and ">" in line) or line.strip().startswith("//") or not line.strip():
        cleaned_lines.append(line)
    elif "," in line:
        cleaned = re.sub(r"\s*,\s*", ",\t", line.strip())
        # Prepend one tab (4 spaces) indentation for data lines
        cleaned_lines.append("\t\t" + cleaned)
    else:
        cleaned_lines.append(line)

with open(file_path, "w") as f:
    f.write("\n".join(cleaned_lines))
