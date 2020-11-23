#!/bin/bash

DB="database"

printf "\n1. Removing table...\n"
psql -d $USER -q -f drop_tables.sql
printf "\ndone\n"
