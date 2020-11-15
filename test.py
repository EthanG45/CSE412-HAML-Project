import sql
# from faker import Faker
# fake = Faker()


db = sql.Database()

# works

# all artists, albums, musician, recordlabel

# works

# insertRecordLabel("arvin","1973-11-06","ggbois",2005) #11/6/1973
# print(sqlReadAny("SELECT companyName, recordLabelId FROM recordLabel WHERE recordLabelId=2002"))


# printAllSongs()
# searchSong("top that")
#updateSongSourceLink('top that', 'EDM', 1, 'this.com', 'frederick-velez.com' ,2005, 615)
# print(sqlReadAny("SELECT * FROM recordLabel"))
# deleteRecordLabel('Arvin','1973-11-06','ggbois',2002)
# print(searchSong("top that"))
#db.insertSong('100', '1001', 'BestAlbum', 'https://fortnite.com')

#db.insertRecordLabel('ASU', '1973-11-06', 'Arizona', '2010')
#db.insertSong("Banana", "fruit", "100", "2006", "2020")
#db.deleteSong("Banana")
#db.insertAlbum('100', '1005', 'Bad Album')
#INSERT INTO recordLabel(companyName, dateEstablished, labelLocation, recordLabelId) VALUES('Microsoft', '1973-11-06', 'Seattle', '1001');
#db.insertRecordLabel('Banana', '1973-11-05', 'My Backyard', '1005')
#db.deleteRecordLabel('Arvin')
#db.updateRecordLabel('NAU', 'Arizona', 'ASU')
#temp = db.getAllSongs()
#with open("outfile.log", "w") as f:
 #   f.write("".join(str(temp)))

#db.insertArtist('1011', 'Joshua Webber', '20')
#db.deleteArtist('Joshua Webber')
#db.updateArtist('21', 'Joshua Webber')
#db.insertMusician('1001', '1001', 'Guitar', 'ASU')
#db.deleteMusician('NAU')
#db.updateMusician('Piano', 'NAU', 'ASU')
#print(db.getAllSongs())
#print(db.changeSongUserRating('not that'))

#db.closeConnection()

# print(fake.image_url())
# print(fake.domain_name())

#print(db.getAllSongs())


#db.cur.execute("UPDATE album SET albumDuration = 11, title = 'Good Album' WHERE albumId = 1")
#db.conn.commit()

#print(db.getAllAlbums())