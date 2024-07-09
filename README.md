## Introduction
Use this to backup your important files on a cron schedule. This only works on a windows machine.  

## Installation
### Step 1: Install required libaries.
    `install -r requirements.txt`  

### Step 2: Create an executable file:  
Run the following command to create an executable:  

    `pyinstaller --onefile your_script.py`  

This will create a dist folder with your_script.exe inside it.  

### Step 2:  Create a backup task in Task Scheduler
    Open Task Scheduler:  
    Press Windows + R, type taskschd.msc, and press Enter.  
    Create a Basic Task:  
        In the Task Scheduler, click on "Create Basic Task..." in the right-hand panel.  
        Follow the wizard:  
            Name: Give your backup task a name and description.  
            Trigger: Choose when you want the backup task to start (e.g., daily, weekly, etc.).  
            Action: Choose "Start a program" and browse to your executable file (main.exe).  
            Finish: Review the details and click "Finish" to create the task.  

## Usage
### Step 1:  
Place your shortcuts (.lnk) to the imnportant files in the `file_shortcuts` folder.  

### Step 2:  
The files will be automatically backed up by Windows' Task Scheduler.
