# DoughSaver
Dough Saver - Team Black - CS411W Fall 2023

*** HOW TO GET STARTED AND RUN THE APP FOR THE FIRST TIME BELOW ***

# resources
https://www.makeuseof.com/django-project-clone-run-locally/
https://www.w3schools.com/django/index.php

# clone GitHub project into working directory
git clone https://github.com/jf-100/DoughSaver.git

# Install python 
https://www.python.org/ or check pip --version

# setup a virtual environment using python venv
python -m venv whatever_venv_name

# when making changes now you need to make sure the venv is running
# I had to navigate to the venv Scripts directory and type ". activate" to start it 
# w3schools link above has good info on this

# this will install required dependencies on the venv
pip install -r requirements.txt

# this will list out the dependencies if not already created
pip freeze > requirements.txt

# run this in the project directory to start the web server
python manage.py runserver

# type this in browser to view web server app
http://127.0.0.1:8000/doughsaverapp/

# I added an overkill .gitignore file so you can add your virtual environment name and whatever else in the future
