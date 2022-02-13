# How to
To run the settlement generator, follow that guide from the GDMC competition website: 
    
    https://gendesignmc.wikidot.com/wiki:submission-mcedit

Use the 'Getting started' guide to download Anacoda (set it up too) and install the dependencies.
- I found that this works best on Windows.


## Anaconda
Conda is simply a package manager for data science. Using the install guide from the GDMC competition website, you should have Coda installed with an environment for Python 2.7. Follow the GDMC guide.


## After installing Anaconda
Initialize that Conda terminal with the activated the Python 2.7 environment, 'cd' into the GDMC folder locally on your system.
When in the correct folder use the stater command 
    
    'python mcedit.py' 


## Issues
The Mcedit distribution provided is tricky to work with, and may fail to launch due to any number of reasons.
The best advise is to look in the terminal to find the output from Conda, if any dependencies are required and missing - install them using.

    'conda install <dep>', or
    'pip install <dep>'
    

# Running the code
Getting the code means to simply clone this repo, and 'cd' into it through the Anaconda terminal (only into GDMC-master folder)
    
Then start mcedit using
    
    python mcedit.py
    
As a command from the GDMC directory

Then, select a saved Minecraft level (saved locally), within the level select an area of the world upon which to generate a settlement.
Click the filter (spray bottle icon) button in the bottom menu, select the 'Settlement generator' filter, click apply, wait.

The code may execute over a few minutes, do not interact with Mcedit during the application of the filter (generating the settlement) as this tends to freeze the application. Simply wait (< 10 mins) for the filter to complete.


## Prerequisite
The application of filters requires that the game Minecraft version 1.8 has been executed locally, with a game started (world generated), the longer the game gets to generate the world when started, the more space you will have to generate a settlement.

To switch Minecraft use the launcher, click the 'Installations' tab then click 'New installation' give it a catchy name, and select version 1.8 under the 'versions dropdown menu, click 'Create' and start playing!
