import PySimpleGUI as sg
import matplotlib.pyplot as plt
import re
import sql
import time
from faker import Faker
fake = Faker()


db = sql.Database()

# print(int(round(time.time())))
# db.insertSongWhileKnowingAlbum('take under budget', 'GOOD SONG', 'OREO', 2000)
# print(db.sqlReadAny("SELECT A.artistName FROM Artist A, Contains C, Song S, Played P, Musician M WHERE S.title = 'not that' AND S.songId = C.songId AND C.albumId = P.albumId AND P.musicianId = M.musicianId AND M.artistId = A.artistId"))
# print(db.findRecordLabelBySongName('hundred school'))
# print(db.sqlReadAny("SELECT R.companyName FROM musician M, played P1, publishes P2, recordLabel R WHERE M.musicianId = P1.musicianId AND P1.albumId = P2.albumId AND P2.recordLabelId = R.recordLabelId AND M.instrument = 'Drums'"))
# print(db.findcompanyNameByBandName('SlateBlue character'))
# print(db.findListOfCompanyNameByInstrument('Drums'))
# print(db.searchArtist('Darlene Lewis'))
# print(db.searchMusician('SlateBlue character'))
# db.insertRecordLabel('Oreo', '2020-11-20',"Texas's house")
# print(db.sqlReadAny("SELECT * FROM recordLabel WHERE companyName = 'Oreo';"))
# print(db.deleteRecordLabel('Aaarvin'))
# artistName, age, instrument, band, albumDuration, title
# db.insertArtist('AATEST',20, 'NO', 'NO','NO')
# print(db.getAllArtists())
# print(db.findLocationByAlbumName('NO'))
# db.deleteArtist('aatest')
# print(db.sqlReadAny("SELECT * FROM recordLabel"))
#print(db.sqlReadAny("SELECT S.title, A.title, A1.artistName, S.genre, S.songDuration, S.sourceLink, S.releaseYear, R.averageRating, R.numOfRating, R.userRating FROM song S, rating R, album A, contains C, artist A1, made M WHERE S.songID = R.songID AND C.songID = S.songID AND C.albumID = A.albumID AND M.albumId = A.albumID AND M.artistId = A1.artistId AND S.title LIKE '%AAARamon%'"))

# Ethan=# SELECT * FROM song WHERE title = 'AAAA Ramon Song';
#       title      |  genre  | songduration |   songid   |    sourcelink    | releaseyear 
# -----------------+---------+--------------+------------+------------------+-------------
#  AAAA Ramon Song | Country |          390 | 1606047302 | smith-daniel.com |        2018

# print(db.getAllArtists())
# print(db.getAllArtists())
# CLEAR MY TERMINAL
#db.insertAlbum(100, 'zzz')
# print(db.getAllAlbums())
#db.deleteRecordLabel('oreo 7')
# db.deleteAlbum('zzzzzzz')
# db.deleteAlbum('third career ahead')
#print(db.getAllRecordLabels())
#db.deleteRecordLabel('AAlbert new cOmpany')
# print(db.allAlbumName()[0][0])
# db.createSongAndAlbum('zzzzalbum', 'please work', 'rock', 2009)
#print(db.getAllSongs())
#db.updateAlbum('updated prepare', 100, 'value its prepare')
# print(db.findLocationByAlbumName('value its prepare'))
#print(db.getAllSongs())
#db.updateSong('zAbg', 'country', 100, 2007, 'yourself media')
#print(db.getAllRecordLabels())
#db.updateRecordLabel('zman', 'Arizona', 'YellowGreen')
#print(db.getAllArtists())
#db.updateArtist(60, 'Zachary Nelson')
# print(db.sqlReadAny("SELECT R.companyName, A.title, R.dateEstablished, R.labelLocation FROM recordLabel R, publishes P, album A, Contains C, Song S WHERE P.recordLabelID = R.recordLabelID AND S.songID = C.songID AND C.albumID = A.albumID AND A.albumID = P.albumID AND LOWER(S.title) = 'able seat' "))
# print(db.sqlReadAny("SELECT R.companyName, A.title, R.dateEstablished, R.labelLocation FROM recordLabel R, publishes P, album A, Contains C, Song S WHERE S.songID = C.songID AND C.albumID = A.albumID AND A.albumID = P.albumID AND P.recordLabelID = R.recordLabelID AND LOWER(S.title) = 'able seat'"))
# print(db.allInstName())
#print(db.getAllArtists())
#db.updateArtist('zzarvin', 60, 'Guitar', 'ASU', 'Zachary Perez')
# print(db.sqlReadAny("SELECT DISTINCT genre FROM song GROUP BY genre"))
# print(db.topTenSongsByUser()[0][3])
# print(db.allGenre())
# fig, ax = plt.subplots()
# for i in range(10):
#     ax.barh(db.topTenSongsByUser()[i][3], db.topTenSongsByUser()[i][7], 0.5)
#     # plt.bar(db.topTenSongsByUser()[i][3], db.topTenSongsByUser()[0][8])
# plt.show()
