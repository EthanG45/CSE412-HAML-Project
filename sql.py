from faker import Faker
import getpass
import psycopg2
from string import Template
from psycopg2 import OperationalError

fake = Faker()

#fake.image_url()
# fake.domain_name()

# Database
class Database:
    # init
    def __init__(self):
        self.userName = getpass.getuser()
        self.conn = psycopg2.connect(database=self.userName, user=self.userName,
                                     host='/tmp', port='8888')
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    # exit
    def closeConnection(self):
        self.cur.close()
        self.conn.close()

    
    def getItems(self):
        result = []
        for i in self.cur:
            result.append(i)
        return result

    def selectQuery(self, table, args, ):
        query = "SELECT * FROM "
        query += table

        if len(args) > 0:
            query += " WHERE "
            query += ' AND'.join(args)

        query += ";"
        self.cur.execute(query)

        return self.getItems()

    #works
    def sqlTopTenSongs(self):
        self.cur.execute(
            "SELECT song.title, rating.averageRating FROM song JOIN rating ON rating.songId = song.songId ORDER BY rating.averageRating DESC LIMIT 10")
        return self.getItems()
    
    #works
    def sqlTopTenAlbums(self):
        self.cur.execute(
            "SELECT album.title, rating.averageRating FROM album JOIN rating ON rating.albumId = album.albumId ORDER BY rating.averageRating DESC LIMIT 10")
        return self.getItems()

    def joinTable(self):
        self.cur.execute(
            "SELECT * FROM song NATURAL JOIN rating AS table1")
        return self.getItems()
    
    #works
    def changeSongAverageRating(self, songName, rating):
        self.conn.set_session(autocommit=True)
        try:
            self.cur.execute("SELECT S.songID FROM Song S, Rating R where S.songID = R.songID and S.title ='%s'" %(songName))
            song_id = self.getItems()[0][0]
            self.cur.execute("UPDATE Rating SET averageRating= %i WHERE songID = %i" %(rating, song_id))
            print('Updated Average Rating with ', rating)
        except Exception as e:
	        print(e)
    
    #works
    def changeSongUserRating(self, songName, rating):
        self.conn.set_session(autocommit=True)
        try:
            self.cur.execute("SELECT S.songID FROM Song S, Rating R where S.songID = R.songID and S.title ='%s'" %(songName))
            song_id = self.getItems()[0][0]
            self.cur.execute("UPDATE Rating SET userRating= %i WHERE songID = %i" %(rating, song_id))
            print('Updated User Rating with ', rating)
        except Exception as e:
	        print(e)

    #works
    def getSongUserRating2(self, songName):
	    try:
		    self.cur.execute("SELECT S.title, R.averageRating From song S, rating R WHERE S.title = '%s' and S.songID = R.SongID" % (songName))
		    return self.getItems()
	    except Exception as e:
		    print(e)

    #works
    def updateSongSourceLink(self,title, genre, songId, newSourceLink, oldSourceLink, releaseYear, songDuration):
        self.conn.set_session(autocommit=True)
        try:
            self.cur.execute("UPDATE song SET sourceLink= '" + newSourceLink + "'" + "WHERE song.title= '" + title + "'" + "AND songId= '"
                        + str(songId) + "'" + "AND genre = '" + genre +
                        "'" + "AND releaseYear= '" + str(releaseYear) + "'"
                        + "AND songDuration= '" + str(songDuration) + "'" + "AND sourceLink= '" + oldSourceLink + "'")
            print('Updated: Replaced ', oldSourceLink, ' with ', newSourceLink)
        except Exception as e:
            print(e)

    #works - works on GUI
    def searchSong(self, songName):
        try:
            self.cur.execute("SELECT S.title, S.genre, S.sourceLink, S.releaseYear, R.numOfRating, R.averageRating FROM song S, rating R WHERE S.songID = R.songID AND title = '%s'" % (songName))
            return self.getItems()
        except:
            return "Song not found"

   #works - works on GUI
    def searchAlbum(self, albumName):
        try:
            self.cur.execute(
                "SELECT title, albumDuration, coverArtURL FROM album WHERE title = '%s'" % (albumName))
            return self.getItems()
        except:
            return "Album not found"

    #works - works on GUI
    def searchMusician(self, bandName):
        try:
            self.cur.execute(
                "SELECT A.artistName, A.age, M.instrument, M.band FROM musician M, artist A WHERE M.artistId = A.artistId AND band = '%s'" % (bandName))
            return self.getItems()
        except:
            return "Musician not found"

     #works - works on GUI 
    def searchArtist(self, artistName):
        try:
            self.cur.execute(
                "SELECT artistName, age, knownFor FROM Artist A, Made M WHERE A.artistID = M.artistID AND artistName = '%s'" % (artistName))
            return self.getItems()
        except:
            return "Artist not found"
    
    #works - works on GUI
    def searchRecordLabel(self, companyName):
        try:
            self.cur.execute(
                "SELECT companyName, dateEstablished, labelLocation FROM recordLabel WHERE companyName = '%s'" % (companyName))
            return self.getItems()
        except:
            return "RecordLabel not found"

    # works - works on GUI
    def getAllSongs(self):
        try:
            self.cur.execute("SELECT S.title, S.genre, S.songduration, S.sourcelink, S.releaseyear, R.averageRating FROM song S, rating R WHERE S.songID = R.songID ORDER BY S.title")
            return self.getItems()
        except:
            return "Failed to fetch library"
    #works
    def sqlReadAny(self,query):
        self.cur.execute(query)
        return self.getItems()

    #works - works on GUI
    def getAllArtists(self):
        result = []
        self.cur.execute("SELECT A.artistName, A.age, M.knownFor, M2.instrument, M2.band FROM Artist A, Made M, Musician M2 WHERE A.artistID = M.artistID AND A.artistID = M2.artistID ORDER BY A.artistName")
        return self.getItems()
    
    #works - works on GUI
    def getAllAlbums(self):
        result = []
        self.cur.execute("SELECT title, albumDuration, coverArtURL FROM album")
        return self.getItems()

    #works
    def getAllMusicians(self):
        result = []
        self.cur.execute("SELECT * FROM musician")
        return self.getItems()
    
    #works - works on GUI
    def getAllRecordLabels(self):
        result = []
        self.cur.execute("SELECT companyName, dateEstablished, labelLocation FROM recordLabel")
        return self.getItems()
    
    #works
    def getAllRatings(self):
        result = []
        self.cur.execute("SELECT * FROM rating")
        return self.getItems()
    
    #works
    def insertAlbum(self, albumDuration, albumId, title):
        try:
            self.cur.execute("INSERT INTO album(albumDuration, albumId, title, coverArtURL) VALUES( '" +
                albumDuration + "', '" + albumId + "', '" + title + "', '" + fake.image_url() + "')")
            #print("Album inserted")
        except Exception as e:
            print(e)
    
    #works
    def deleteAlbum(self, title):
        try:
            self.cur.execute("DELETE FROM album WHERE title= '" + str(title) + "'")
            print("Deleted Row with ", title)
        except Exception as e:
            print(e)

    #works
    def updateAlbum(self, newTitle, newDuration, oldTitle):
        try:
            self.cur.execute("UPDATE album SET title = '" + newTitle + "', albumDuration = '" + newDuration +
            "'WHERE title = '" + oldTitle + "'")
            self.conn.commit()
        except Exception as e:
            print(e)

    #works
    def insertSong(self, title, genre, songDuration, songId, releaseYear):
        try:
            self.cur.execute("INSERT INTO song(title, genre, songDuration, songId, sourceLink, releaseYear) VALUES( '" +
                title + "', '" + genre + "', '" + songDuration + "', '" + songId + "', '" + fake.domain_name() +  "', '" + releaseYear + "')")
        except Exception as e:
            print(e)

    #works
    def deleteSong(self, songName):
        try:
            self.cur.execute("DELETE FROM song WHERE title = '" + songName + "'")
        except Exception as e:
            print(e)

    #works
    def updateSong(self, newTitle, newGenre, newDuration, newYear, oldTitle):
        try:
            self.cur.execute("UPDATE song SET title = '" + newTitle + "', genre = '" + newGenre + "', songDuration = '" + newDuration + "', releaseYear = '" + newYear +
            "'WHERE title = '" + oldTitle + "'")
            self.conn.commit()
        except Exception as e:
            print(e)

    #works
    def insertRecordLabel(self, companyName, dateEstablished, labelLocation, recordLabelId):
        try:
            self.cur.execute("INSERT INTO recordLabel(companyName, dateEstablished, labelLocation, recordLabelId) VALUES( '" +
                companyName + "', '" + dateEstablished + "', '" + labelLocation + "', '" + recordLabelId + "')")
        except Exception as e:
            print(e)

    #works
    def deleteRecordLabel(self, companyName):
        try:
            self.cur.execute("DELETE FROM recordLabel WHERE companyName = '" + companyName + "'")
        except Exception as e:
            print(e)
    
    #works
    def updateRecordLabel(self, newCompanyName, newLabelLocation, oldCompanyName):
        try:
            self.cur.execute("UPDATE recordLabel SET companyName = '" + newCompanyName + "', dateEstablished = '" + fake.date() + "', labelLocation = '" + newLabelLocation +
            "'WHERE companyName = '" + oldCompanyName + "'")
            self.conn.commit()
        except Exception as e:
            print(e)

    #works
    def insertArtist(self, artistId, artistName, age):
        try:
            self.cur.execute("INSERT INTO artist(artistId, artistName, age) VALUES( '" +
                artistId + "', '" + artistName + "', '" + age + "')")
        except Exception as e:
            print(e)
    
     #works
    def deleteArtist(self, artistName):
        try:
            self.cur.execute("DELETE FROM artist WHERE artistName = '" + artistName + "'")
        except Exception as e:
            print(e)
    
    #works updated age only
    def updateArtist(self, newAge, artistName):
        try:
            self.cur.execute("UPDATE artist SET age = '" + newAge +
            "'WHERE artistName = '" + artistName + "'")
            self.conn.commit()
        except Exception as e:
            print(e)
    
    #works
    def insertMusician(self, artistId, musicianId, instrument, band):
        try:
            self.cur.execute("INSERT INTO musician(artistId, musicianId, instrument, band) VALUES( '" +
                artistId + "', '" + musicianId + "', '" + instrument + "', '"+ band + "')")
        except Exception as e:
            print(e)
    
    #works
    def deleteMusician(self, band):
        try:
            self.cur.execute("DELETE FROM musician WHERE band = '" + band + "'")
        except Exception as e:
            print(e)
    
    #works updated age only
    def updateMusician(self, newInstrument, newBand, oldBand):
        try:
            self.cur.execute("UPDATE musician SET instrument = '" + newInstrument + "', band =  '" + newBand +
            "'WHERE band = '" + oldBand + "'")
            self.conn.commit()
        except Exception as e:
            print(e)

    #works - Complex Queries Series
    def findArtistBySongName(self, songName):
        try:
            self.cur.execute("SELECT A.artistName FROM Artist A, Contains C, Song S, Played P, Musician M WHERE S.title = '%s' AND S.songId = C.songId AND C.albumId = P.albumId AND P.musicianId = M.musicianId AND M.artistId = A.artistId" % (songName))
            return self.getItems()
        except Exception as e:
            print(e)

     #works - Complex Queries Series
    def tenMusicWithWorstRating(self):
        try:
            self.cur.execute(
                "SELECT song.title, rating.averageRating FROM song JOIN rating ON rating.songId = song.songId ORDER BY rating.averageRating ASC LIMIT 10")
            return self.getItems()
        except Exception as e:
            print(e)

    #works - Complex Queries Series
    def songNameWithYearByArtist(self, artistName, releaseYear):
         try:
             self.cur.execute("SELECT S.title, S.releaseYear FROM Artist A, Contains C, Song S, Played P, Musician M WHERE S.releaseYear >= %i AND A.artistName = '%s' AND S.songId = C.songId AND C.albumId = P.albumId AND P.musicianId = M.musicianId AND M.artistId = A.artistId" % (releaseYear, artistName))
             return self.getItems()
         except Exception as e:
             print(e)

    #works
    def findcompanyNameByAlbumName(self, albumName):
         try:
             self.cur.execute("SELECT R.companyName FROM recordLabel R, publishes P, album A WHERE A.albumID = P.albumID AND P.recordLabelID = R.recordLabelID AND A.title = '%s'"% (albumName))
             return self.getItems()
         except Exception as e:
             print(e)

    #works
    def findLocationByAlbumName(self, albumName):
         try:
             self.cur.execute("SELECT R.labelLocation FROM recordLabel R, publishes P, album A WHERE A.albumID = P.albumID AND P.recordLabelID = R.recordLabelID AND A.title = '%s'"% (albumName))
             return self.getItems()
         except Exception as e:
             print(e)
            
    #works
    def findRecLebDateByAlbumName(self, albumName):
         try:
             self.cur.execute("SELECT R.dateEstablished FROM recordLabel R, publishes P, album A WHERE A.albumID = P.albumID AND P.recordLabelID = R.recordLabelID AND A.title = '%s'"% (albumName))
             return self.getItems()
         except Exception as e:
             print(e)

    #works
    def findcompanyNameBySongName(self, songName):
         try:
             self.cur.execute("SELECT R.companyName FROM recordLabel R, publishes P, album A, Contains C, Song S WHERE S.songID = C.songID AND C.albumID = A.albumID AND A.albumID = P.albumID AND P.recordLabelID = R.recordLabelID AND S.title = '%s'" % (songName))
             return self.getItems()
         except Exception as e:
             print(e)

    #works
    def findcompanyNameByBandName(self, bandName):
         try:
             self.cur.execute("SELECT R.companyName FROM musician M, played P1, publishes P2, recordLabel R WHERE M.musicianId = P1.musicianId AND P1.albumId = P2.albumId AND P2.recordLabelId = R.recordLabelId AND M.band = '%s'" % (bandName))
             return self.getItems()
         except Exception as e:
             print(e)
    #works
    def findListOfCompanyNameByInstrument(self, instName):
         try:
             self.cur.execute("SELECT R.companyName FROM musician M, played P1, publishes P2, recordLabel R WHERE M.musicianId = P1.musicianId AND P1.albumId = P2.albumId AND P2.recordLabelId = R.recordLabelId AND M.instrument = '%s'" % (instName))
             return self.getItems()
         except Exception as e:
             print(e)
       


# todo rate a song

# todo list all songs/albums from an artist

#