# How to
To run the settlement generator, follow that guide from the GDMC competition website: https://gendesignmc.wikidot.com/wiki:submission-mcedit
Use the 'Getting started' guide to download Anacoda (set it up too) and install the dependencies.
- I found that this works best on Windows.


## Anaconda
Conda is simply a package manager for data science. Using the install guide from the GDMC competition website, you should have Coda installed with an environment for Python 2.7.

## Using my 'Filters'
Filters are the term used by McEdit to describe Python code to execute in the simulated game environment.
This project applies a filter to execute settlement generation within the game world (not in real time).

Simply copy/paste the content of the 'stock-filters' folder into your local folder of the same name within the GDMC folder as cloned from the 'Getting started' guide.


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
To run the code make sure that all the filters (Python code from the zip) is pasted into the local folder
  
    ~GDMC/stock-filters/
    
Then start mcedit using
    
    python mcedit.py
    
As a command from the GDMC directory

Then, select a saved Minecraft level (saved locally), within the level select an area of the world upon which to generate a settlement.
Click the filter (spray bottle icon) button in the bottom menu, select the 'Settlement generator' filter, click apply, wait.

The code may execute over a few minutes, do not interact with Mcedit during the application of the filter (generating the settlement) as this tends to freeze the application. Simply wait (< 10 mins) for the filter to complete.


## Prerequisite
The application of filters requires that the game Minecraft version 1.8 has been executed locally, with a game started (world generated), the longer the game gets to generate the world when started, the more space you will have to generate a settlement.

To switch Minecraft use the launcher, click the 'Installations' tab then click 'New installation' give it a catchy name, and select version 1.8 under the 'versions dropdown menu, click 'Create' and start playing!
