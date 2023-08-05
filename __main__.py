import os
from api import Api
from logs import logger
from dotenv import load_dotenv
from updater import update_readme


load_dotenv ()
AUTO_RUN_GIT = os.getenv ('AUTO_RUN_GIT') == 'True'
CURRENT_DIR = os.path.dirname (os.path.abspath (__file__))

def main (): 
    
    commands_to_save = []        
    
    # Get api data
    api = Api ()
    projects_data = api.get_data ()
    
    if projects_data:
        logger.info ("\nUpating projects...")
        for project_id, project_data in projects_data.items ():
            
            # Get project data
            project_name = project_data['name']
            project_location = project_data['location']
            markdown = project_data.get ('markdown', None)
            
            # Status
            logger.info (f"\nUpdating '{project_name}' in path '{project_location}'...")
            
            # Validate markdown
            if not markdown:
                logger.info (f"\tNo markdown data for project '{project_name}'")
                continue
            
            new_commands = update_readme (project_location, markdown)
            if new_commands:
                commands_to_save += new_commands
            
            # Update project status
            updated = api.update_project_status (project_id)
            if updated:
                logger.info (f"Status updated")
            else:
                logger.error (f"Status not updated")
    
    if commands_to_save:
        commands_text = ' &\n'.join (commands_to_save)
        with open  (os.path.join (CURRENT_DIR, 'git-commands.bat'), 'w') as file:
            file.write (f"{commands_text}")
        logger.info ("\nCommands to update projects saved in 'git-commands.bat'")
        
    logger.info ("Done.")
    
if __name__ == "__main__":
    main()