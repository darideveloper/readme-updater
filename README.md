<div><a href='https://github.com/darideveloper/readme-updater/blob/master/LICENSE' target='_blank'>
                <img src='https://img.shields.io/github/license/darideveloper/readme-updater.svg?style=for-the-badge' alt='MIT License' height='30px'/>
            </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a><a href='https://www.twitch.tv/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Twitch&color=b9a3e3&logo=Twitch&logoColor=ffffff&label=' alt='Twitch' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://raw.githubusercontent.com/darideveloper/readme-updater/master/logo.png' alt='Readme Updater' height='80px'/>



# Readme Updater

Update repo README.md files, using the data stores in the **[Dari Dev's Projects Manager](https://github.com/darideveloper/portfolio_backend)**

Project type: **personal**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#relatedprojects'>Related Projects</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li>
<li><a href='#roadmap'>Roadmap</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://requests.readthedocs.io/en/latest/' target='_blank'> <img src='https://requests.readthedocs.io/en/latest/_static/requests-sidebar.png' alt='Requests' title='Requests' height='50px'/> </a><a href='https://www.mkdocs.org/user-guide/writing-your-docs/' target='_blank'> <img src='https://cdn.svgporn.com/logos/markdown.svg' alt='Markdown' title='Markdown' height='50px'/> </a><a href='https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html' target='_blank'> <img src='https://cdn.svgporn.com/logos/bash-icon.svg' alt='Bash' title='Bash' height='50px'/> </a></div>

# Related projects

<div align='center'><a href='https://github.com/darideveloper/portfolio' target='_blank'> <img src='https://github.com/darideveloper/portfolio/blob/master/imgs/logo.png?raw=true' alt='Portfolio Frontend' title='Portfolio Frontend' height='50px'/> </a><a href='None' target='_blank'> <img src='None' alt='Portfolio Backend' title='Portfolio Backend' height='50px'/> </a></div>

# Details

The project detect new changes to saved in the README.mc files, for project stores in **[Dari Dev's Projects Manager](https://github.com/darideveloper/portfolio_backend)**, get the new markdown data, commit it and push the changes to the remote repo.

You should have registered your porjects in the dashboard and a local copy in your pc.

# Install

## Third party modules

Install all modules from pip: 

``` bash
$ pip install -r requirements.txt
```

## Programs

To run the project, the following software must be installed:

* Git
* Python >= 3.10

# Settings

## Enviroment variables

In this file (*.env*), are the main options and settings of the project.

1. Create a **.env** file, and place the following content

```bash
API_USER_NAME = {your-username-here}
API_PASSWORD = {your-password-here}
```

### API_USER_NAME

User name of the project manager dashboard. 

### API_PASSWORD

Password of the project manager dashboard. 

*Note: you can see as reference the **sample.env** file*

## Dashboard

In the dashboard, be sure to save the Location PC as the absolute path of the local copy of the project, in your pc. 

[INSERT IMAGE HERE]

# Run

Run the project folder with python: 
```sh
python .
```

Or run the main file:
```sh
python __main__.py
```

## Run in loop

If you want to tun the bot in loop (one or multiple times each day), I suggest you to use tools to run the script all days at specific time, like [Task Scheduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page) for windows, [Cron](https://www.google.com/search?q=linux+cronjobs&oq=linux+cronjobs&aqs=chrome..69i57.3719j0j1&sourceid=chrome&ie=UTF-8) for Linux or [Jenkins](https://www.jenkins.io/) for both systems

# Roadmap

* [X] Detect updated projects
* [X] Get project data
* [X] Get markdown from each project
* [X] Update local README.md file. 
* [X] Update project status in dashboard

