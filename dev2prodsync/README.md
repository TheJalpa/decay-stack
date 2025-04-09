## Instruction

#Step 1
fill out dzvars.py
This contains the directories for:

- clonedir: This is your cloned git repo or working directory. This would be if you are working from git for your dayz server. Otherwise if you have a central location, it would be that. This assumes your location has 2 folders. map and profiles. Within these are the contents for your workflow. This would be mod settings, map settings, etc.
- devprofiledir: This will be the location of your profile directory for your dev server. Example, if you are running a local dayzserver this might be /mnt/c/steamcmd/steamapps/common/DayZServer/profiles/
- devmaploc: This will be the location of your map directory for your dev server. Example, if running a local server this might be /mnt/c/steamcmd/steamapps/common/DayZServer/mpmissions/empty.deerisle/
- prodprofiledir: This script would be placed on your prod server where you'll be cloning your workload and then this becomes the working profile directory for that. Example /home/steam/steamcmd/steamapps/common/DayZServer/profiles/
- prodmaploc: Same as above, this is the working prod location of your production server. Example: /home/steam/steamcmd/steamapps/common/DayZServer/mpmissions/empty.deerisle/

#Step 2
Run the script
The following would execute this against dev with a dry run, showing you all potentially changed files.
python3 sync.py --dzbranch dev --dzrun dry

The following would execute this against dev and change files
python3 sync.py --dzbranch dev

The usage for this script is:

python3 sync.py --dzbranch branchname --dzrun value (true/false)

The current potential values for dzbranch are dev and prod. The current potential values for dzrun are true/false.
You can, of course, change these if you'd like and modify these in such a way that you could have more branches.
I'm not aware of anyone running a server setup where they are running dev/staging/prod. Most run a dev/prod for those who test, and 99% of servers don't even do that.

#What's the idea behind this?

Workflow! My current workflow consists of a local dayzserver I run on my PC for testing, with my centralized code in a git repo.
From here, I rsync my changes from my git repo to that directory via this script. I then restart my server, and test my changes.
When my changes have been completed and I'm happy with them, I do a pull request to my git repo, merge to main.
I log into my production machine, git pull from main, run this script for prod, restart my server, and enjoy my tested changes.

Step by step:

- Create github private repo for your project
- Create github project key and save to custom location (you'll use this to pull your private project on your prod server)
- Using your current projection workload on your server, copy the contents of profiles and your map into that git repo.
- Remove all unecessary files within git directory for maps and profiles. Database files, logs, save information (Unless you WANT these, but I don't recommend it) and also make sure you have no private info in there. Should you ever accidentally make it public you expose that, so be cautious what you put in your git repos. Security is important! An example of this is, I have a working load of my events files, quests files for dayz expansion, and some of my mod settings files, but nothing else.
- Copy the sync and dzvars scripts to working locations on both your dev machine and prod server.
- Fill out dzvars.py with the locations accordingly. At some point in the near future I'll probably add some other support like ftp or ssh. Right now I just do this stuff locally.
- Git checkout -b featurebranchname and make the changes I want to test out
- Run the script for dev with a dry run, checking that it looks good.
- Run the script for dev if I'm happy with the dry run.
- Start up the local dayz server, test out my changes, make sure I'm happy.
- Git add . & git commit -m "my changes"
- Make a pull request in git, merge my changes to main, double checking very carefully that I made all intended changes I meant to.
- Log into prod, git pull from main.
- Run script for prod, restart server. Enjoy fresh changes that have been tested without worrying about human clerical error or guessing if stuff is correct.

An simplified example of this in a working lifecycle would be:

- Production server profiles folder and maps folder are copied to your central working location. Example, your git repo in vscode.
- Utilizing a git feature branch, make the changes you want in your working directory.
- Run script for dev, test changes.
- Push and merge changes to main.
- Checkout on prod, run script for prod. Restart server.

This ensures that you:

- Have a history of your changes you make to your server.
- You can roll back changes to a known working version of your server for specific mod configurations.
- You can review all your changes before pushing them to prod.
- You can create a local test environment that you can test without the hassle of testing your server in prod and pissing off your players.
