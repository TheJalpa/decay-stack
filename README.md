# thejalpa-dz-tools

## Overview and purpose

The idea behind this repository was to create a set of tools for server owners
who may not be familiar with xml or other server related functions to be able
to have tools available to them they can use to create a dedicated server.

These are primarily for linux based systems, however, xml stitcher and typescraper works platform agnostic.
I will add an update in the near future for windows servers to utilize moddownloader and modinstaller.
Currently there is not a large need for these, as most windows users are using GUI based "buy and go" platforms
that do most of this work for you. So it is not a large priority right now.

As I have often been told, "If you've gotta do it more than a handful of times... automate it."
I have yet to automate that saying.

Being able to easily run some scripts to manage your server should make life much easier.
As I started to dive into working on DayZ servers, I noticed there was an inherent lack of tools out there.
Some of the higher end stuff let you basically drag and drop and provide guis. But for those making
a server from scratch, it's a new experience and some of this stuff can be cumbersome.

Copying and pasting xml stuff, cleaning the files, dragging and dropping, moving stuff over, changing things...
Yeah it gets old.

So here's some tools to make your life easier.

## Things you'll need

Python 3.
If you're on linux, you can yum or apt-get it.

If you are on windows, you can go to the microsoft store and download python.

Once you have installed it, open up a command prompt or shell and type "python3" and make sure it works.
Control+Z to exit out. If that works, congrats, you're ready to use these tools!

For more information: [You can click here for a guide](https://wiki.python.org/moin/BeginnersGuide)

## XML Stitcher

This tool does exactly what it sounds like it does. It will piece together XML files for you.

This tool is used to stitch and add xml files for a first time only. Keep in mind, if you run this
more than once, with the same xml files, you'll duplicate the entries. This is intended to help
server owners add mods for first time use. So if you add mod1234.xml, and then run the script again,
you'll be adding mod1234.xml to types.xml twice, which will cause duplication errors.

At some point in the near future this script will have the ability to do more.
I'll even add duplicate entry checks at some point. But.... one thing at a time.

**How to use it:**

- Place the xml files you will need to add to your types.xml in the "modsxml" folder.
  _(Special note, some mods have xml files for specific maps so be sure it's what you need. Make sure no duplicate filenames.)_
- Make sure you've added notations in your XML files. For instance <!-- Name of my mod here so I know where it starts --> _These are not removed_
- Place your types.xml for your map in the "originalxml" folder. This will be your xml from your map.
  _(Note, this can be found in basedirectory/mpmissions/missionname/db/types.xml)_

**What will this do?**
XML Stitcher is using basic regex to look for patterns in your XML files. It will iterate through all files
within the modsxml folder. It will then clean them and append them to your types.xml file.

Example:

./modsxml/mod123.xml
./modsxml/mod456.xml
./modsxml/mod684.xml

./originalxml/types.xml

Script is executed. All 3 mod xml files above are cleaned. /types is removed at the bottom of types.xml
and is then appended with the mod xmls above. It is then appended with /types and closed.

No further action should be needed, you can use this types.xml then on your server.  
It is highly recommended you go ahead and backup the original types.xml on your server as types.backup
or something along those lines, so if you ever need to revert changes, you can.

However, the script never touches types.xml within the "originalxml" folder, so it remains untouched so you can
make a backup or keep that there safely.

## typescraper

**What will this do?**
Typescraper is a script that is intended to scrape the patterns of type names out of your types.xml and exports it into a usable list of type class names.
This allows you to then cut the pieces you want out and add them to your trader as you need.

Since there is not currently a way to know if something is say a vehicle/tool/food etc in DayZ in types.xml, you will need to do the rest.
However, this helps you scrape all of these types out so you can make a list, thus ensuring you do not miss anything.

One of the largest issues I see when adding mods is that many mod creators do not keep consistent naming conventions,
thus leading to missing things in traders. Sorting through every mod types.xml and your server xml is extremely cumbersome.

This alleviates some of that frustration so you can just cut and paste what you need, and sort the rest and never forget it again!

In the future I will add a feature to search up specific patterns, but right now it just dumps your entire types.xml

## Mod downloader

**What will this do?**
The name is pretty self explanatory. This has two scripts. The first one is mod downloader. It utilizes two filess: manualmods.txt and modlist.txt.
modlist is the list of all mods you want to use on your server. The manualmods is a list of mods that either you are using and can't get from marketplace,
or perhaps if you are having to manually add them to the server because steamcmd times out as they are too big.

An example of this would be if I use modABC, and it is 800kb, but also another mod, modXYZ and it is 8gb. For some reason if XYZ times out, and we have to manually add it,
we add it to manualmods.txt.

We then use a new line for each mod. Lastly, we fill out the dayzvars.py which includes our steam creds, where our dayzserver lives, and where steam lives...Then we run the script.

The script will first iterate through all of our modlist and create a shell script to download these mods. We execute this script when we are ready (it doesn't do it automatically for this reason)
and then once our mods are downloaded successfully, we run the modinstaller.py. This will symbolically link the new mod, copy the bikeys over to your keys folder for you, and all you need to do is restart your server.

## Special notes

**Do you have a service example?**
One thing I learned early on was instead of trying to start the dayzserver itself with the executable and pointing just to the config,
it was easier to actually make the system service point to the startup script, so that using my automation for mod installations
and for changes could simply reflect those changes once the script was ran. Now I can go pull and add mods, restart, and it points to that script.

Mine is different than what Bohemia's tutorial recommended but it's worked better for my purposes with automation.

```
Wants=network-online.target
After=syslog.target network.target nss-lookup.target network-online.target

[Service]
ExecStart=/gaming/dayzscripts/startdayz.sh
-BEpath=battleeye
WorkingDirectory=/gaming/dayzserver/
LimitNOFILE=100000
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s INT $MAINPID
User=steam
Group=steam
Restart=on-failure
RestartSec=5s
StandardOutput=/var/log/dayz.log
StandardError=/var/log/dayzerror.log

[Install]
WantedBy=multi-user.target
```
