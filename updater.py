import os
import subprocess
from logs import logger
from dotenv import load_dotenv

load_dotenv ()
AUTO_RUN_GIT = os.getenv ('AUTO_RUN_GIT') == 'True'

def update_readme (path:str, markdown:str):
    """ Update README.md file in a project and push changes

    Args:
        path (str): path to project
        markdown (str): markdown data to write in README.md file
    """
    
    # Move to project location
    os.chdir (path)

    # Create readme file if not exists
    files = os.listdir ()
    if 'README.md' not in files:
        with open ('README.md', 'w') as file:
            file.write ('')
        logger.info (f"README.md file created")    
    
    # Write data in readme file 
    with open ('README.md', 'w', encoding='UTF-8') as file:
        file.write (markdown)
    logger.info (f"README.md file updated")
    
    # Git commands
    if AUTO_RUN_GIT: 
        path_formatted = path.replace ('\\', '/')
    else:
        path_formatted = path
    commands = [
        f'git config --global --add safe.directory {path_formatted}',
        'git checkout master',
        'git pull origin master',
        'git add README.md',
        'git commit -m "Update README.md with Bot"',
        'git push origin master',
    ]
        
        
    if AUTO_RUN_GIT:
        # auto commit changes
        logger.info ("---------- Git ----------")
        for command in commands:
            logger.info (f"Executing: '{command}'")
            result = subprocess.getoutput (command)
            logger.info (f"Result: '{result}'")
        logger.info ("--------------------------")
    else:
        # Add cd to commands
        commands.insert (0, f'cd {path_formatted}')
        
        # Return commands
        return commands
        
        
    