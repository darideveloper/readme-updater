import os
from api import Api
from updater import update_readme

def main (): 
    
    apì = Api ()
    projects_data = apì.get_data ()
    
    print ("Upating projects...")
    for project_id, project_data in projects_data.items ():
        
        # Get project data
        project_name = project_data['name']
        project_location = project_data['location']
        markdown = project_data.get ('markdown', None)
        
        # Validate markdown
        if not markdown:
            print (f"\tNo markdown data for project '{project_name}'")
            continue
        
        print (f"\tUpdating '{project_name}' in path '{project_location}'...")
        update_readme (project_location, markdown)
    
if __name__ == "__main__":
    main()