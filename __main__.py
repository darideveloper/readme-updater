import os
from api import Api
from updater import update_readme
from dotenv import load_dotenv

load_dotenv ()
AUTO_RUN_GIT = os.getenv ('AUTO_RUN_GIT') == 'True'
CURRENT_DIR = os.path.dirname (os.path.abspath (__file__))

def main (): 
    
    commands_to_save = []        
    
    # Get api data
    api = Api ()
    projects_data = api.get_data ()
    
    if projects_data:
        print ("\nUpating projects...")
        for project_id, project_data in projects_data.items ():
            
            # Get project data
            project_name = project_data['name']
            project_location = project_data['location']
            markdown = project_data.get ('markdown', None)
            
            # Status
            print (f"\nUpdating '{project_name}' in path '{project_location}'...")
            
            # Validate markdown
            if not markdown:
                print (f"\tNo markdown data for project '{project_name}'")
                continue
            
            new_commands = update_readme (project_location, markdown)
            if new_commands:
                commands_to_save += new_commands
            
            # Update project status
            updated = api.update_project_status (project_id)
            if updated:
                print (f"Status updated")
            else:
                print (f">> Error: Status not updated")
    
    if commands_to_save:
        commands_text = ' &\n'.join (commands_to_save)
        with open  (os.path.join (CURRENT_DIR, 'git-commands.bat'), 'w') as file:
            file.write (f"{commands_text}")
        print ("\nCommands to update projects saved in 'git-commands.bat'")
        
    print ("Done.")
    
if __name__ == "__main__":
    main()