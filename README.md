# thejalpa-dz-tools

## Overview and purpose

The idea behind this repository was to create a set of tools for server owners
who may not be familiar with xml or other server related functions to be able
to have tools available to them they can use to create a dedicated server.

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
