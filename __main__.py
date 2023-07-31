import os
from api import Api
from updater import update_readme

def main (): 
    
    api = Api ()
    projects_data = api.get_data ()
    
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
        
        print (f"\n\t>> Updating '{project_name}' in path '{project_location}'...")
        update_readme (project_location, markdown)
        
        # Update project status
        updated = api.update_project_status (project_id)
        if updated:
            print (f"\tStatus updated")
        else:
            print (f"\tStatus not updated")
    
if __name__ == "__main__":
    main()