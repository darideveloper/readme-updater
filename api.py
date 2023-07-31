import os
import json
from dotenv import load_dotenv
import requests

load_dotenv () 
API_USER_NAME = os.getenv ('API_USER_NAME')
API_PASSWORD = os.getenv ('API_PASSWORD')
API_BASE = os.getenv ('API_BASE')

class Api ():
    
    def __init__ (self):
        self.token = None
        self.projects_data = {}
    
    def __login__ (self):
        """ Login with crdentials and get token """
        
        # Login
        url = f"{API_BASE}/api-token-auth/"
        payload = {
            'username': API_USER_NAME,
            'password': API_PASSWORD
        }
        res = requests.post (url, data=payload)
        if res.status_code != 200:
            print ('Login failed: invalid crdentials')
            quit()
        
        # Get tokeb from json
        res_json = res.json ()
        if 'token' not in res_json:
            print ('Login failed: token not found')
            quit()
            
        self.token = res_json['token']
        print ('Login success')

    def __query_projects__ (self):
        """ Get update status of all projects """
        
        print ("Getting projects data...")
                
        url = f"{API_BASE}/projects-sumary/"
        while True:
            
            # Get projects data from api
            res = requests.get (url, headers={'Authorization': 'Token ' + self.token})
            res_json = res.json ()
            
            # Get next link and results
            url = res_json['next']
            results = res_json['results']
            
            # Save id, status and path
            for result in results:
                id = result['id']
                name = result['name']
                updated_remote = result['updated_remote']
                location_pc = result['location_pc']
                
                if not updated_remote and location_pc:
                    self.projects_data[id] = {
                        'name': name,
                        'location_pc': location_pc
                    }
            
            # Show status
            projects_count = len (self.projects_data)
            print (f"\t{projects_count} projects found")
            
            # Debug
            break
            
            # End loop if no more pages
            if not url:
                break 
    
    def __query_markdown__ (self):
        """ get markdown data of all projects """
        
        print ("Getting markdown data...")
        
        # Update each project
        for project_id, project_data in self.projects_data.items():
            
            project_name = project_data['name']
            
            print (f"\t{project_name}...")
            
            url = f"{API_BASE}/project-markdown/?id={project_id}"
            res = requests.get (url, headers={'Authorization': 'Token ' + self.token})
            
            # Validate response status
            if res.status_code != 200:
                print (f"\tError getting markdown data for project '{project_name}'")
                continue
            
            # Get markdown
            res_json = res.json ()
            markdown = res_json['data']
            
            # Save markdown in dict
            self.projects_data[project_id]["markdown"] = markdown
            
    def get_data (self) -> list:
        """ Get projects data who need update: id, name, location_pc, markdown

        Returns:
            list: dicts with projects data
        """
    
        self.__login__ ()
        self.__query_projects__ ()
        self.__query_markdown__ ()
        return self.projects_data        
    
if __name__ == '__main__':
    api = Api ()
    projects_data = api.get_data ()
    print ()