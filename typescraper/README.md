## Instruction

Place your types.xml into this directory with the script. Example: dayzserverlocation/mpmissions/empty.deerisle/db/types.xml
Place your TraderConfig.txt into this directory with the script. Example: profilelocation/Trader/TraderConfig.txt

Run the script `python3 typescraper.py`

#Part 1: Output of tradertypes
The output will be tradertypes.xml
Utilize this file for all your trader needs as it is a cleaned, exact replica of all type names
in your types.xml.

This is useful if you have not yet added items to your trader, and want the types names, but don't feel like digging through 50,000 lines in your types file.

#Part 2: Sorted diff of missing types

Massive shout out to [tknorris23](https://github.com/tknorris23)
The following section was made and modified with their help:

The script will continue to run and will diff against your trader file. What it is looking for in this case is any missing objects within TraderConfig.txt
that do not match a type from types.xml. So if you forgot something that exists in types, but not in the trader, these output files will show up for you.

From here, sorted.txt (or output.txt if you're on windows, I'm too lazy to do powershell but put a request in if you want) will appear which is a diff file that looks for all missing types in your trader file.
This is so you can go back to your TraderConfig.txt and edit missing items.

Keep in mind, this does not discriminate against types, so you'll likely see entries for Zombies, animals and the like.
However, it will also give you all of the missing items. This is especially helpful if you recently added mods and thought
you got all items, but perhaps are missing some at your trader.

Helping you get these ahead of time instead of players saying, "Hey you're missing xyz at the trader."
