import os
from logs import logger
import requests
from dotenv import load_dotenv

load_dotenv () 
API_USER_NAME = os.getenv ('API_USER_NAME')
API_PASSWORD = os.getenv ('API_PASSWORD')
API_BASE = os.getenv ('API_BASE')
DEBUG = os.getenv ('DEBUG') == 'True'

class Api ():
    
    def __init__ (self):
        self.projects_data = {}
        self.header = {}
        
        if DEBUG: 
            logger.info (">>Debug mode<<")
    
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
            logger.info ('Login failed: invalid crdentials')
            quit()
        
        # Get tokeb from json
        res_json = res.json ()
        if 'token' not in res_json:
            logger.info ('Login failed: token not found')
            quit()
            
        token = res_json['token']
        self.header = {'Authorization': f'Token {token}'}
        logger.info ('Login success')

    def __query_projects__ (self):
        """ Get update status of all projects """
        
        logger.info ("\nGetting projects data...")
                
        url = f"{API_BASE}/projects-sumary/"
        while True:
            
            # Get projects data from api
            res = requests.get (url, headers=self.header)
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
                        'location': location_pc
                    }
            
            # Debug
            if DEBUG:
                break
            
            # End loop if no more pages
            if not url:
                break 
            
        # Show status
        projects_count = len (self.projects_data)
        logger.info (f"\t{projects_count} projects found")
    
    def __query_markdown__ (self):
        """ get markdown data of all projects """
        
        if self.projects_data:
            
            logger.info ("\nGetting markdown data...")
            
            # Update each project
            for project_id, project_data in self.projects_data.items():
                
                project_name = project_data['name']
                
                logger.info (f"\t{project_name}...")
                
                url = f"{API_BASE}/project-markdown/?id={project_id}"
                res = requests.get (url, headers=self.header)
                
                # Validate response status
                if res.status_code != 200:
                    logger.error (f"\tError getting markdown data for project '{project_name}'")
                    continue
                
                # Get markdown
                res_json = res.json ()
                markdown = res_json['data']
                
                # remove backslashes
                markdown = markdown.replace ('\\', '').replace("\r\n", "\n")
                
                # Save markdown in dict
                self.projects_data[project_id]["markdown"] = markdown
            
    def update_project_status (self, project_id:int) -> bool:
        """ Update status project using api

        Args:
            project_id (int): project id
            
        Returns:
            bool: True if status updated, False if not
        """
        
        url = f"{API_BASE}/project-update-remote/"
        res = requests.post (url, headers=self.header, data={'id': project_id})
        
        if res.status_code != 200:
            logger.error (f"Error updating project status {res.data}")
            return False
        
        return res.status_code == 200
        
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
    
    # Debug get projects data api when run directly
    api = Api ()
    projects_data = api.get_data ()
    
    # Debug update project status api when run directly
    api.update_projet_status (projects_data.keys ()[0])
    logger.info ()
    