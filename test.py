import PySimpleGUI as sg
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
# print(db.sqlReadAny("SELECT companyName, dateEstablished, labelLocation FROM recordLabel WHERE companyName = 'NavajoWhite'")[0][2])
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
