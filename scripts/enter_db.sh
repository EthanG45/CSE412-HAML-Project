#!/bin/bash

if [ ! pg_isready ]; then
    printf "Error no database running!"
    exit 1
fi

printf "\n1. Enter the database:\n"
psql -d $USER # enter the database (a rather trivial command)
