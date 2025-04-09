## Instructions

Disclaimer: At this time, this script is for linux administrators.
A new version will be included in the near future for windows admins as well.
However, as most windows server hosts are using "gui-to-go" style, most of this is
automated and not needed for them.

It will still be added, just not a high priority right now. There are few tools out there
for linux admins.

Also, please note that this set of scripts is intended to live in the directory you'll be pointing your script to.

In my case I have a /gaming/dayzserver folder on one of my mounted drives, and my scripts live in /gaming/dayzscripts
and then I have my system service pointing to the startup script there, which points to my dayzserver.
This allows me a clean place to modify scripts without touching my server files accidentally.

You can do this however you'd like, but this has worked well for me.

Instructions:

1.  Populate dayzvars.py - this is imported into the following scripts. It is worth noting that
    in order to even download mods for dayzservers on steamcmd you need steam credentials. You also
    need to tell the script where your dayzserver lives, and where your steam lives.

This is so the script can copy items from the workshop to your server, and symbolically link them.

2.  Populate modlist.txt with a list of all mods you want installed and will use on your server.
    This should be mods you can download from steamcmd. Each should be a new line.

Example:

```
123456
456789
482827
```

Save this file.

3.  Populate the manualmods.txt with a list of all mods you want installed and use on your server.
    However these are mods that you have to manually add to your server via ftp or other means,
    likely due to steamcmd timeouts or another reason. Example: You need a mod that's 5 gigs and steamcmd times out when dling it.
    So you just manually install it instead, but the script needs to know about it to prime your start script.

Example:

```
877666
786786
989898
```

Save this file.

4.  Execute the script for moddownload. `python3 moddownloader.py` - a new script will be generated.
    This will be called dayzmods.sh. You can then execute this file `bash dayzmods.sh` and it will download
    all necessary mods for your server.

5.  Execute the script for modinstaller. `python3 modinstaller.py` - From here you can check your startdayz.sh script
    and make sure it has updated for your server. You should see all your variables for your startup script, the list of mods in order.

### Special note

If you find you need a very specific startup order, this script appends the mods in the order you put them in modlist.txt.
So if you need to make sure the order stays the same every time, order them accordingly in modlist.txt.

```

```
