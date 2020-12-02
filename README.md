# CodeDigger Backend

## Features

#### Setting Environment First Time
Below commands will setup the environment for the first time.

#### Windows
```
py -m pip install --user virtualenv
py -m venv env
```
#### Linux
```
python3 -m pip install --user virtualenv
python3 -m venv env
```

#### Starting Virtual Env. and Setting up the Project
Below are the commands for project Initialization into your local computer
#### For Windows
```
. env/Scripts/activate -- If using gitbash
. env\Scripts\activate -- If using Windows Powershell
pip install -r requirements.txt
cd codedigger
py manage.py migrate
py manage.py runserver
```
- This would start the development server

#### For Linux
```
source env/bin/activate
pip3 install -r requirements.txt
cd codedigger
python3 manage.py migrate
python3 manage.py runserver
```
- This would start the development server 

### Leaving the virtual environment
```
deactivate
```
