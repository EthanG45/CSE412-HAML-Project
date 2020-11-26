#!/bin/bash

DB="database"

out=$(pg_isready | grep 'no response' | cut -f1)

# if [ -n out ]; then
#     printf "Database is not running!\n"
#     exit 1
# fi

if [ ! -d "./database" ]; then
    printf "Error no database to delete!"
    exit 1
fi

printf "\n1. Removing table...\n"
if psql -d $USER -q -f ./postgres-setup/drop_tables.sql; then
    printf "\n2. Removing database...\n"
    rm -rf ./database
fi

printf "\ndone\n"
