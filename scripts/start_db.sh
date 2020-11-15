#!/bin/bash

DB="database"

if [ ! pg_isready ]; then
    printf "Error no database running!"
    exit 1
fi

printf "\n1. Start database:\n"
pg_ctl -D $DB -o '-k /tmp' start # starts the server on the port YYYYY, using ./database as data folder
