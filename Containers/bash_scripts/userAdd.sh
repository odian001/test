#!/bin/bash
datetime=$(date "+%Y-%m-%d %H:%M:%S")
if [ $# -ne 5 ]; then
    echo "Error: The script requires exactly 5 arguments."
    echo "Usage: $0 'email' 'password' 'Name' 'zip code' 'address'"
    exit 1
fi
docker run -it --network doughsavernetwork --rm mariadb mariadb -hdoughsaverdb -uroot -p'1qaz!QAZ' DoughSaverDB -e "insert into Customer (Email, Password, Name, PrimaryLocation, Address, CreationDate, LastLogin) Values('$1', '$2', '$3', '$4', '$5', '$datetime', '$datetime')"
