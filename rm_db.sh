#!/bin/bash

DB="database"

# if [ ! pg_isready ]; then
#     printf "Error no database running!"
#     exit 1
# fi

if [ ! -d "./database" ]; then
    printf "Error no database to delete!"
    exit 1
fi

printf "\n1. Removing table...\n"
psql -d $USER -q -f drop_tables.sql

printf "\n2. Removing database...\n"
rm -rf ./database

printf "\ndone\n"
