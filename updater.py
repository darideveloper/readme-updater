import os

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
        print (f"README.md file created")    
    
    # Write data in readme file 
    with open ('README.md', 'w', encoding='UTF-8') as file:
        file.write (markdown)
    print (f"README.md file updated")
        
    # Commit changes
    path_formatted = path.replace ('\\', '/')
    print ("---------- Git ----------")
    os.system (f'git config --global --add safe.directory {path_formatted}')
    os.system ('git pull origin master')
    os.system ('git add README.md')
    os.system ('git commit -m "Update README.md with Bot"')
    os.system ('git push origin master')
    print ("--------------------------")
    