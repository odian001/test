#!/bin/bash
docker run -it --network doughsavernetwork --rm mariadb mariadb -hdoughsaverdb -uroot -p'1qaz!QAZ' DoughSaverDB -e "Select IngredientID, StoreID, CurrentPrice, UpdateTimestamp from PriceData"
