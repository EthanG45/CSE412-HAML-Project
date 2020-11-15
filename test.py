import sql
# from faker import Faker
# fake = Faker()


db = sql.Database()


#print(db.sqlReadAny("SELECT A.artistName FROM Artist A, Contains C, Song S, Played P, Musician M WHERE S.title = 'not that' AND S.songId = C.songId AND C.albumId = P.albumId AND P.musicianId = M.musicianId AND M.artistId = A.artistId"))
#print(db.findRecordLabelBySongName('hundred school'))
# print(db.sqlReadAny("SELECT R.companyName FROM musician M, played P1, publishes P2, recordLabel R WHERE M.musicianId = P1.musicianId AND P1.albumId = P2.albumId AND P2.recordLabelId = R.recordLabelId AND M.instrument = 'Drums'"))
# print(db.findcompanyNameByBandName('SlateBlue character'))
print(db.findListOfCompanyNameByInstrument('Drums'))