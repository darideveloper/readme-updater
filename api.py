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
    
    def login (self):
        """ Login with crdentials and get token """
        
        # Login
        url = API_BASE + '/api-token-auth/'
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

    def query_projects (self):
        """ Get update status of all projects """
        
        print ("Getting projects data...")
                
        url = API_BASE + '/projects/'
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
                        'updated_remote': updated_remote,
                        'location_pc': location_pc
                    }
            
            # End loop if no more pages
            if not url:
                break
            
    
    def get_markdown (self):
        pass
    
if __name__ == '__main__':
    api = Api ()
    api.login ()
    api.query_projects ()