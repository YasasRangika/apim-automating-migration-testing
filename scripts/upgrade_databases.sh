#!/bin/bash

#**************************Rename below db names to regdb, userdb and amdb before hand-over*******************************
db="amdb1"

mysql -u root -D$db < 'data/migration_scripts/apimgt-db-migration-scripts-'"$1"'to'"$2"'/mysql.sql';
