# DoughSaver
Dough Saver - Team Black - CS411W Fall 2023

*** HOW TO SETUP THE CONTAINERS TO RUN IN YOUR ENVIRONMENT ***


# Clone GitHub project into working directory
git clone https://github.com/jf-100/DoughSaver.git

# Requirements
Docker - https://www.linux.com/topic/desktop/how-install-and-use-docker-linux/


# Setting up the mariadb container
docker pull mariadb
docker network create doughsavernetwork
docker run --detach --network doughsavernetwork --name mockdata --env MARIADB_USER=dsuser --env MARIADB_PASSWORD='samplepassword' --env MARIADB_ROOT_PASSWORD='Quackblack75!' mariadb:latest

# Load data into the mariadb container.
docker exec -i mockdata sh -c 'exec mariadb -uroot -p"Quackblack75!"' < /location/of/mysql/backup.sql

# Run an interactive session with the mariadb container
docker run -it --network doughsavernetwork --rm mariadb mariadb -hmockdata -uroot -p DoughSaverDB

# Creating a docker image for the web scraper (Walmart only).
# Execute this in the pyDocker directory
docker build -t ds_scraper .

# Executing the web scraper. (Currently checks the database for the 12 most outdated items that don't have the isPaused flag set and scrapes their prices)
* Change ***/location/of/output_data/*** to the path of the output_data directory provided in the pyDocker directory *
docker run -v ./output_data/:***/location/of/output_data*** --network doughsavernetwork --rm ds_scraper:latest


# Setting up the Django container
#Run the below command from the Django directory with requirements.txt
docker build -t django .

docker run --network doughsavernetwork -d -p 8000:8000 django