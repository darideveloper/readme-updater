import os
from api import Api
from updater import update_readme

def main (): 
    
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
            
            update_readme (project_location, markdown)
            
            # Update project status
            updated = api.update_project_status (project_id)
            if updated:
                print (f"Status updated")
            else:
                print (f">> Error: Status not updated")
            
    print ("Done.")
    
if __name__ == "__main__":
    main()