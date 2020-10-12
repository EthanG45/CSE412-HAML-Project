#!/bin/bash

rm ./output/*.log

if [ ! -d "./output" ]; then
    mkdir output
fi

printf "Demo Queries for CSE 412 Midterm Report...\n"
printf "See ./output"

# 1. COUNT OPERATIONS
printf "\nAlbum:\n" >./output/demo1_count.log
psql -d $USER -q -c "SELECT count(distinct(albumId)) FROM album;" >>./output/demo1_count.log
printf "\nRecord Label:\n" >>./output/demo1_count.log
psql -d $USER -q -c "SELECT count(distinct(recordLabelId)) FROM recordLabel;" >>./output/demo1_count.log
printf "\nArtist:\n" >>./output/demo1_count.log
psql -d $USER -q -c "SELECT count(distinct(artistId)) FROM artist;" >>./output/demo1_count.log
printf "\nMusician:\n" >>./output/demo1_count.log
psql -d $USER -q -c "SELECT count(distinct(musicianId)) FROM musician;" >>./output/demo1_count.log
printf "\nContains:\n" >>./output/demo1_count.log
psql -d $USER -q -c "SELECT count(distinct(songId)) FROM contains;" >>./output/demo1_count.log
printf "\nSong:\n" >>./output/demo1_count.log
psql -d $USER -q -c "SELECT count(distinct(songId)), count(title) AS TitleCount FROM song;" >>./output/demo1_count.log
printf "\nPlayed:\n" >>./output/demo1_count.log
psql -d $USER -q -c "SELECT count(distinct(musicianId)) FROM played;" >>./output/demo1_count.log
printf "\nMade:\n" >>./output/demo1_count.log
psql -d $USER -q -c "SELECT count(distinct(albumId)) FROM made;" >>./output/demo1_count.log
printf "\nRating:\n" >>./output/demo1_count.log
psql -d $USER -q -c "SELECT count(distinct(albumId)) FROM rating;" >>./output/demo1_count.log
printf "\nPublishes:\n" >>./output/demo1_count.log
psql -d $USER -q -c "SELECT count(distinct(recordLabelId)) FROM publishes;" >>./output/demo1_count.log

# 2. READ OPERATIONS
printf "List 20 Artist that are 20 years old:\n" >> ./output/demo2_read.log
psql -d $USER -q -c "SELECT artistName, age FROM artist WHERE age = 20 LIMIT 20" >> ./output/demo2_read.log
printf "\nList 20 Songs that released on 2009:\n" >> ./output/demo2_read.log
psql -d $USER -q -c "SELECT TITLE, GENRE,RELEASEYEAR  FROM song WHERE song.RELEASEYEAR = 2009 LIMIT 20" >> ./output/demo2_read.log
printf "\nList 20 Rap Songs:\n" >> ./output/demo2_read.log
psql -d $USER -q -c "SELECT TITLE, GENRE FROM song WHERE song.GENRE = 'Rap' LIMIT 20" >> ./output/demo2_read.log

# 3. CREATE/UPDATEish Operations AND 4. DELETE OPERATIONS
printf "UPDATE, INSERT, and DELETE:\n" >>./output/demo3_insert_and_delete.log
psql -d $USER -q -c "INSERT INTO recordLabel(companyName, dateEstablished, labelLocation, recordLabelId) VALUES('Microsoft', '1973-11-06', 'Seattle', '1001');" >>./output/demo3_insert_and_delete.log
psql -d $USER -q -c "INSERT INTO song(title, genre, songDuration, songId, sourceLink, releaseYear) VALUES('WAP', 'Rap', '100', '2000','wap.com', '2020');" >>./output/demo3_insert_and_delete.log
psql -d $USER -q -c "INSERT INTO album(albumDuration, albumId, title, coverArtURL) VALUES('100', '1001', 'BestAlbum', 'https://fortnite.com');" >>./output/demo3_insert_and_delete.log
psql -d $USER -q -c "UPDATE album SET albumDuration = 10, title = 'Good Album' WHERE albumId = 1;" >>./output/demo3_insert_and_delete.log

psql -d $USER -q -c "SELECT count(distinct(songId)), count(title) AS TitleCount FROM song;" >>./output/demo3_insert_and_delete.log
psql -d $USER -q -c "SELECT count(distinct(albumId)) FROM album;" >>./output/demo3_insert_and_delete.log
psql -d $USER -q -c "SELECT count(distinct(recordLabelId)) FROM recordLabel;" >>./output/demo3_insert_and_delete.log

psql -d $USER -q -c "DELETE FROM song WHERE songId=2000 AND releaseYear=2020 AND sourceLink='wap.com';" >>./output/demo3_insert_and_delete.log
psql -d $USER -q -c "DELETE FROM album WHERE albumId=1001 AND albumDuration=100;" >>./output/demo3_insert_and_delete.log
psql -d $USER -q -c "DELETE FROM recordLabel WHERE companyName='Microsoft' AND labelLocation='Seattle' AND recordLabelId=1001;" >>./output/demo3_insert_and_delete.log

psql -d $USER -q -c "SELECT count(distinct(songId)), count(title) AS TitleCount FROM song;" >>./output/demo3_insert_and_delete.log
psql -d $USER -q -c "SELECT count(distinct(albumId)) FROM album;" >>./output/demo3_insert_and_delete.log
psql -d $USER -q -c "SELECT count(distinct(recordLabelId)) FROM recordLabel;" >>./output/demo3_insert_and_delete.log

# 5. SEARCH OPERATIONS/ INTERESTING QUERIES
printf "Top 10 songs by average rating:\n" >> ./output/demo4_search.log
psql -d $USER -q -c "SELECT song.title, rating.averageRating FROM song JOIN rating ON rating.songId = song.songId ORDER BY rating.averageRating DESC LIMIT 10;" >> ./output/demo4_search.log
printf "\nsongs where average rating is less then 1.5\n" >>./output/demo4_search.log
psql -d $USER -q -c "SELECT song.title, rating.averageRating FROM song JOIN rating ON rating.songId = song.songId WHERE rating.averageRating < 1.5 LIMIT 20;" >> ./output/demo4_search.log
printf "\nfind songs high let and its rating\n" >>./output/demo4_search.log
psql -d $USER -q -c "SELECT song.title, rating.averageRating FROM song JOIN rating ON rating.songId = song.songId WHERE song.title = 'high let';" >> ./output/demo4_search.log
