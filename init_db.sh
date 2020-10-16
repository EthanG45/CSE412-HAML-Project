#!/bin/bash

DB="database"
CWD=$(pwd) # get current path for use in the sql COPY command. SQL COPY occurs in a different location than this shellscript ¯\_(ツ)_/¯

# todo check if the port 8888 has a running process
# todo finish fleshing out the rest of the shell scripts to be safe!
# todo kill port 8888

if [ -d "./database" ]; then
    printf "Error database already exists!"
    exit 1
fi

printf -- "1. Creating database...\n"
mkdir $DB
initdb $DB # initializes a database structure in the folder ./database

printf "\n2. Starting database...\n"
pg_ctl -D $DB -o '-k /./tmp' start # starts the server on the port YYYYY, using ./database as data folder
createdb $USER                     # creates a database, with your current username on your machine as its name

printf "\n3. Creating tables...\n"
psql -d $USER -q -f create_tables.sql

printf "\n4. Importing data...\n"
psql -d $USER -q -c "COPY album FROM '$CWD/data/Album.csv' DELIMITER ',' CSV;"
psql -d $USER -q -c "COPY artist FROM '$CWD/data/Artist.csv' DELIMITER ',' CSV;"
psql -d $USER -q -c "COPY contains FROM '$CWD/data/Contains.csv' DELIMITER ',' CSV;"
psql -d $USER -q -c "COPY made FROM '$CWD/data/Made.csv' DELIMITER ',' CSV;"
psql -d $USER -q -c "COPY musician FROM '$CWD/data/Musician.csv' DELIMITER ',' CSV;"
psql -d $USER -q -c "COPY played FROM '$CWD/data/Played.csv' DELIMITER ',' CSV;"
psql -d $USER -q -c "COPY recordLabel FROM '$CWD/data/RecordLabel.csv' DELIMITER ',' CSV;"
psql -d $USER -q -c "COPY song FROM '$CWD/data/Song.csv' DELIMITER ',' CSV;"
psql -d $USER -q -c "COPY rating FROM '$CWD/data/Rating.csv' DELIMITER ',' CSV;"
psql -d $USER -q -c "COPY publishes FROM '$CWD/data/Publishes.csv' DELIMITER ',' CSV;"

if [ ! -d "./tmp" ]; then
    mkdir tmp
fi

printf "\n5. Testing tables...\n"
printf "\nAlbum:\n" >>./tmp/test_tables.log
psql -d $USER -q -c "SELECT count(distinct(albumId)) FROM album;" >>./tmp/test_tables.log
printf "\nRecord Label:\n" >>./tmp/test_tables.log
psql -d $USER -q -c "SELECT count(distinct(recordLabelId)) FROM recordLabel;" >>./tmp/test_tables.log
printf "\nArtist:\n" >>./tmp/test_tables.log
psql -d $USER -q -c "SELECT count(distinct(artistId)) FROM artist;" >>./tmp/test_tables.log
printf "\nMusician:\n" >>./tmp/test_tables.log
psql -d $USER -q -c "SELECT count(distinct(musicianId)) FROM musician;" >>./tmp/test_tables.log
printf "\nContains:\n" >>./tmp/test_tables.log
psql -d $USER -q -c "SELECT count(distinct(songId)) FROM contains;" >>./tmp/test_tables.log
printf "\nSong:\n" >>./tmp/test_tables.log
psql -d $USER -q -c "SELECT count(distinct(songId)), count(title) AS TitleCount FROM song;" >>./tmp/test_tables.log
printf "\nPlayed:\n" >>./tmp/test_tables.log
psql -d $USER -q -c "SELECT count(distinct(musicianId)) FROM played;" >>./tmp/test_tables.log
printf "\nMade:\n" >>./tmp/test_tables.log
psql -d $USER -q -c "SELECT count(distinct(albumId)) FROM made;" >>./tmp/test_tables.log
printf "\nRating:\n" >>./tmp/test_tables.log
psql -d $USER -q -c "SELECT count(distinct(albumId)) FROM rating;" >>./tmp/test_tables.log
printf "\nPublishes:\n" >>./tmp/test_tables.log
psql -d $USER -q -c "SELECT count(distinct(recordLabelId)) FROM publishes;" >>./tmp/test_tables.log

num=$(grep -o -i 1000 tmp/test_tables.log | wc -l)

rm -rf tmp

if [ $num -eq 11 ]; then
    printf "\n6. Tables were generated properly"
    printf "\ndone\n"
    exit 0
else
    printf "\n6. Tables were not generated properly!"
    printf "\n Removing database! Please run init_db.sh again!"
    ./rm_db.sh
    printf "\ndone\n"
    exit 1
fi
