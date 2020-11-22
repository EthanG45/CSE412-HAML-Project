import random
from random import randint
import getpass
import time
import re
import psycopg2
import random
from faker import Faker
from string import Template
from psycopg2 import OperationalError

fake = Faker()

# fake.image_url()
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

    # works
    def replaceApostrophe(self, myString):
        myString = re.sub('(?<=[a-z])\'(?=[a-z])', '', myString)
        return myString

    def selectQuery(self, table, args, ):
        query = "SELECT * FROM "
        query += table

        if len(args) > 0:
            query += " WHERE "
            query += ' AND'.join(args)

        query += ";"
        self.cur.execute(query)

        return self.getItems()

    def joinTable(self):
        self.cur.execute(
            "SELECT * FROM song NATURAL JOIN rating AS table1")
        return self.getItems()

    # works
    def changeSongAverageRating(self, songName, rating):
        self.conn.set_session(autocommit=True)
        try:
            self.cur.execute(
                "SELECT S.songID FROM Song S, Rating R where S.songID = R.songID and LOWER(S.title) ='%s'" % (songName.lower()))
            song_id = self.getItems()[0][0]
            self.cur.execute(
                "UPDATE Rating SET averageRating= %i WHERE songID = %i" % (rating, song_id))
            print('Updated Average Rating with ', rating)
        except Exception as e:
            print(e)

    # works
    def changeSongUserRating(self, songName, rating):
        self.conn.set_session(autocommit=True)
        try:
            self.cur.execute(
                "SELECT S.songID FROM Song S, Rating R where S.songID = R.songID and LOWER(S.title) ='%s'" % (songName.lower()))
            song_id = self.getItems()[0][0]
            self.cur.execute(
                "UPDATE Rating SET userRating = %i WHERE songID = %i" % (rating, song_id))
        except Exception as e:
            print(e)
    
    def changeSongNumOfRating(self, songName, numOfRating):
        self.conn.set_session(autocommit=True)
        try:
            self.cur.execute(
                "SELECT S.songID FROM Song S, Rating R where S.songID = R.songID and LOWER(S.title) ='%s'" % (songName.lower()))
            song_id = self.getItems()[0][0]
            self.cur.execute(
                "UPDATE Rating SET numOfRating = %i WHERE songID = %i" % (numOfRating, song_id))
            print('Updated User Rating with ', rating)
        except Exception as e:
            print(e)
    
    def changeWholeRating(self, songName, rating):
        self.conn.set_session(autocommit=True)
        averageRating = randint(10, 50)/10
        try:
            self.cur.execute(
                "SELECT S.songID FROM Song S, Rating R where S.songID = R.songID and LOWER(S.title) ='%s'" % (songName.lower()))
            song_id = self.getItems()[0][0]
            self.cur.execute(
                "UPDATE Rating SET userRating = %i  WHERE songID = %i" % (rating, song_id))
            self.cur.execute(
                "UPDATE Rating SET averageRating = %f WHERE songID = %i" % (averageRating, song_id))
            self.cur.execute(
                "UPDATE Rating SET numOfRating = numOfRating + 1 WHERE songID = %i" % (song_id))
            print('Updated User Rating with ', rating)
        except Exception as e:
            print(e)

    # works
    def getSongUserRating(self, songName):
        try:
            self.cur.execute(
                "SELECT S.title, R.averageRating From song S, rating R WHERE LOWER(S.title) = '%s' and S.songID = R.SongID" % (songName.lower()))
            return self.getItems()
        except Exception as e:
            print(e)

    # works
    # def updateSongSourceLink(self,title, genre, songId, newSourceLink, oldSourceLink, releaseYear, songDuration):
    #     self.conn.set_session(autocommit=True)
    #     try:
    #         self.cur.execute("UPDATE song SET sourceLink= '" + newSourceLink + "'" + "WHERE song.title= '" + title + "'" + "AND songId= '"
    #                     + str(songId) + "'" + "AND genre = '" + genre +
    #                     "'" + "AND releaseYear= '" + str(releaseYear) + "'"
    #                     + "AND songDuration= '" + str(songDuration) + "'" + "AND sourceLink= '" + oldSourceLink + "'")
    #         print('Updated: Replaced ', oldSourceLink, ' with ', newSourceLink)
    #     except Exception as e:
    #         print(e)

    # works - works on GUI
    def searchSong(self, songName):
        try:
            self.cur.execute(
                "SELECT S.title, S.genre, S.sourceLink, S.releaseYear, R.numOfRating, R.averageRating FROM song S, rating R WHERE S.songID = R.songID AND LOWER(title) = '%s'" % (songName.lower()))
            return self.getItems()
        except:
            return "Song not found"

   # works - works on GUI
    def searchAlbum(self, albumName):
        try:
            self.cur.execute(
                "SELECT title, albumDuration, coverArtURL FROM album WHERE LOWER(title) = '%s'" % (albumName.lower()))
            return self.getItems()
        except:
            return "Album not found"

    # works - works on GUI
    def searchMusician(self, bandName):
        try:
            self.cur.execute(
                "SELECT A.artistName, A.age, M.instrument, M.band FROM musician M, artist A WHERE M.artistId = A.artistId AND LOWER(band) = '%s'" % (bandName.lower()))
            return self.getItems()
        except:
            return "Musician not found"

     # works - works on GUI
    def searchArtist(self, artistName):
        try:
            self.cur.execute(
                "SELECT artistName, age, knownFor FROM Artist A, Made M WHERE A.artistID = M.artistID AND LOWER(artistName) = '%s'" % (artistName.lower()))
            return self.getItems()
        except:
            return "Artist not found"

    # works - works on GUI
    def searchRecordLabel(self, companyName):
        try:
            self.cur.execute(
                "SELECT companyName, dateEstablished, labelLocation FROM recordLabel WHERE LOWER(companyName) = '%s'" % (companyName.lower()))
            return self.getItems()
        except:
            return "RecordLabel not found"

    # works - works on GUI
    def getAllSongs(self):
        try:
            self.cur.execute(
                "SELECT S.title, A.title, S.genre, S.songduration, S.sourcelink, S.releaseyear, R.averageRating, R.numOfRating, R.userRating FROM song S, rating R, album A, contains C WHERE S.songID = R.songID AND C.songID = S.songID AND C.albumID = A.albumID ORDER BY LOWER(S.title)")
            return self.getItems()
        except:
            return "Failed to fetch library"

    # works - works on GUI
    def getAllArtists(self):
        result = []
        self.cur.execute("SELECT A.artistName, A.age, M.knownFor, M2.instrument, M2.band FROM Artist A, Made M, Musician M2 WHERE A.artistID = M.artistID AND A.artistID = M2.artistID ORDER BY LOWER(A.artistName)")
        return self.getItems()

    # works
    def sqlReadAny(self, query):
        self.cur.execute(query)
        return self.getItems()

    # works - works on GUI
    # def getAllArtists(self):
    #     result = []
    #     self.cur.execute("SELECT * FROM artist")
    #     return self.getItems()

    # works - works on GUI
    def getAllAlbums(self):
        result = []
        self.cur.execute(
            "SELECT A.title, A.albumDuration, A.coverArtURL, R.averageRating, R.numOfRating, R.userRating FROM album A, rating R WHERE R.albumId = A.albumId ORDER BY LOWER(title)")
        return self.getItems()

    # works
    def getAllMusicians(self):
        result = []
        self.cur.execute("SELECT * FROM musician")
        return self.getItems()

    # works - works on GUI
    def getAllRecordLabels(self):
        result = []
        self.cur.execute(
            "SELECT companyName, dateEstablished, labelLocation FROM recordLabel ORDER BY LOWER(companyName)")
        return self.getItems()

    # works
    def getAllRatings(self):
        result = []
        self.cur.execute("SELECT * FROM rating")
        return self.getItems()

    # works
    def insertAlbum(self, albumDuration, title):
        albumId = int(round(time.time()))
        coverArtURL = fake.image_url()
        try:
            self.cur.execute("SELECT artistId FROM artist ORDER BY RANDOM() LIMIT 1")
            artistId = self.getItems()[0][0]
            musicianId = artistId
            self.cur.execute("INSERT INTO album(albumDuration, albumId, title, coverArtURL) VALUES(%i, %i,'%s','%s')" % (
                albumDuration, albumId, title, coverArtURL))
            self.cur.execute(
                'SELECT knownFor FROM made WHERE artistId = %i' % (artistId))
            knownFor = self.getItems()[0][0]
            self.cur.execute("INSERT INTO made(knownFor, albumId, artistId) VALUES('%s', %i, %i)" % (
                knownFor, albumId, musicianId))
            self.cur.execute("INSERT INTO played(albumId, musicianId) VALUES( %i, %i)" % (
                albumId, musicianId))
        except Exception as e:
            print(e)

    # works
    def deleteAlbum(self, title):
        try:
            self.cur.execute(
                "SELECT albumId FROM album WHERE LOWER(title) = '%s'" % (title.lower()))
            universalID = self.getItems()[0][0]
            self.cur.execute(
                "DELETE FROM rating WHERE albumId = %i" % (universalID))
            self.cur.execute(
                "DELETE FROM made WHERE albumId = %i" % (universalID))
            self.cur.execute("DELETE FROM album WHERE LOWER(title) = '%s' AND albumId = %i" % (
                title.lower(), universalID))
            self.cur.execute(
                "DELETE FROM played WHERE albumId = %i" % (universalID))
        except Exception as e:
            print(e)

    # works
    def updateAlbum(self, newTitle, newDuration, oldTitle):
        try:
            self.cur.execute("UPDATE album SET title = '" + newTitle + "', albumDuration = '" + newDuration +
                             "'WHERE title = '" + oldTitle + "'")
            self.conn.commit()
        except Exception as e:
            print(e)

    # works
    def insertSong(self, title, genre, releaseYear):
        songDuration = randint(30, 1000)
        userRating = 0
        songId = int(round(time.time()))
        sourceLink = fake.domain_name()
        averageRating = randint(10, 50)/10
        numOfRating = int(randint(1, 100000))
        try:
            self.cur.execute("SELECT albumId FROM album ORDER BY RANDOM() LIMIT 1")
            albumId = self.getItems()[0][0]
            self.cur.execute("INSERT INTO song(title, genre, songDuration, songId, sourceLink, releaseYear) VALUES('%s', '%s', %i, %i,'%s', %i)" % (
                title, genre, songDuration, songId, sourceLink, releaseYear))
            self.cur.execute(
                "INSERT INTO contains(albumId, songId) VALUES( %i, %i)" % (albumId, songId))
            self.cur.execute("INSERT INTO rating(numOfRating, averageRating, userRating, albumId, songId ) VALUES( %i, %i, %i, %i, %i)" % (
                numOfRating, averageRating, userRating, albumId, songId))
        except Exception as e:
            print(e)

    # works
    def deleteSong(self, songName):
        try:
            self.cur.execute(
                "SELECT songId FROM song WHERE LOWER(title) = '%s'" % (songName.lower()))
            universalID = self.getItems()[0][0]
            self.cur.execute(
                "DELETE FROM rating WHERE songId = %i" % (universalID))
            self.cur.execute("DELETE FROM song WHERE LOWER(title) = '%s' AND songId = %i" % (
                songName.lower(), universalID))
            self.cur.execute(
                "DELETE FROM contains WHERE songId = %i" % (universalID))
        except Exception as e:
            print(e)

    # works
    def updateSong(self, newTitle, newGenre, newDuration, newYear, oldTitle):
        try:
            self.cur.execute("UPDATE song SET title = '" + newTitle + "', genre = '" + newGenre + "', songDuration = '" + newDuration + "', releaseYear = '" + newYear +
                             "'WHERE title = '" + oldTitle + "'")
            self.conn.commit()
        except Exception as e:
            print(e)

    # works
    def insertRecordLabel(self, companyName, dateEstablished, labelLocation):
        recordLabelId = int(round(time.time()))
        try:
            self.cur.execute("SELECT albumId FROM publishes ORDER BY RANDOM() LIMIT 1")
            albumId = self.getItems()[0][0]
            self.cur.execute(
                "DELETE FROM publishes WHERE albumId = %i" % (albumId))
            self.cur.execute("INSERT INTO recordLabel(companyName, dateEstablished, labelLocation, recordLabelId) VALUES('%s', '%s', '%s', %i)" % (
                self.replaceApostrophe(companyName), dateEstablished, self.replaceApostrophe(labelLocation), recordLabelId))
            self.cur.execute("INSERT INTO publishes(albumId, recordLabelId) VALUES (%i, %i)" % (
                albumId, recordLabelId))
        except Exception as e:
            print(e)

    # works
    def deleteRecordLabel(self, companyName, date, location):
        try:
            self.cur.execute("SELECT recordLabelId FROM recordLabel WHERE LOWER(companyName) = '%s' AND dateEstablished = '%s' AND  labelLocation = '%s'" % (
                companyName.lower(), date, location))
            universalID = self.getItems()[0][0]
            self.cur.execute(
                "DELETE FROM publishes WHERE recordLabelId = %i" % (universalID))
            self.cur.execute("DELETE FROM recordLabel WHERE LOWER(companyName) = '%s' AND recordLabelId = %i" % (
                companyName.lower(), universalID))
        except Exception as e:
            print(e)

    # works
    def updateRecordLabel(self, newCompanyName, newLabelLocation, oldCompanyName):
        try:
            self.cur.execute("UPDATE recordLabel SET companyName = '" + newCompanyName + "', dateEstablished = '" + fake.date() + "', labelLocation = '" + newLabelLocation +
                             "'WHERE companyName = '" + oldCompanyName + "'")
            self.conn.commit()
        except Exception as e:
            print(e)

    # Works
    def insertArtist(self, artistName, age, instrument, band, title):
        knownFor = title
        coverArtURL = fake.image_url()
        albumDuration = randint(100, 10000)
        artistId = int(round(time.time()))
        musicianId = artistId
        albumId = artistId
        try:
            self.cur.execute("SELECT recordLabelId FROM recordLabel ORDER BY RANDOM() LIMIT 1 ")
            labelID = self.getItems()[0][0]
            self.cur.execute("INSERT INTO artist(artistId, artistName, age) VALUES(%i, '%s', %i)" % (
                artistId, artistName, age))
            self.cur.execute("INSERT INTO musician(artistId, musicianId, instrument, band) VALUES(%i, %i, '%s', '%s')" % (
                artistId, musicianId, instrument, band))
            self.cur.execute("INSERT INTO album(albumDuration, albumId, title, coverArtURL) VALUES(%i, %i,'%s','%s')" % (
                albumDuration, albumId, title, coverArtURL))
            self.cur.execute("INSERT INTO made(knownFor, albumId, artistId) VALUES('%s', %i, %i)" % (
                knownFor, artistId, musicianId))
            self.cur.execute("INSERT INTO played(albumId, musicianId) VALUES( %i, %i)" % (
                albumId, musicianId))
            self.cur.execute(
                "INSERT INTO publishes(albumId, recordLabelId) VALUES(%i, %i)" % (albumId, labelID))
            self.conn.commit()
        except Exception as e:
            print(e)

     # works
    def deleteArtist(self, artistName, age):
        try:
            self.cur.execute("SELECT artistId FROM artist WHERE LOWER(artistName) = '%s' AND age = %i" % (artistName.lower(), age)) 
            universalID = self.getItems()[0][0]
            self.cur.execute(
                "DELETE FROM made WHERE artistId = %i" % (universalID))
            self.cur.execute("DELETE FROM artist WHERE LOWER(artistName) = '%s' AND artistId = %i" % (
                artistName.lower(), universalID))
            self.cur.execute(
                "DELETE FROM played WHERE musicianId = %i" % (universalID))
            self.cur.execute(
                "DELETE FROM musician WHERE musicianId = %i" % (universalID))
            self.cur.execute(
                "DELETE FROM publishes WHERE albumId = %i" % (universalID))
        except Exception as e:
            print(e)

    # works updated age only
    def updateArtist(self, newAge, artistName):
        try:
            self.cur.execute("UPDATE artist SET age = '" + newAge +
                             "'WHERE artistName = '" + artistName + "'")
            self.conn.commit()
        except Exception as e:
            print(e)

    # works
    # def insertMusician(self, instrument, band):
     #   artistId = int(round(time.time()))
      #  musicianId = artistId
        # try:
        #    self.cur.execute("INSERT INTO musician(artistId, musicianId, instrument, band) VALUES( '" +
         #       artistId + "', '" + musicianId + "', '" + instrument + "', '"+ band + "')")
        # except Exception as e:
         #   print(e)

    # Works DO WE NEED IT
    # def deleteMusician(self, band):
     #   try:
      #      self.cur.execute("DELETE FROM musician WHERE band = '" + band + "'")
        # except Exception as e:
        #    print(e)

    # works updated age only
    # def updateMusician(self, newInstrument, newBand, oldBand):
     #   try:
      #      self.cur.execute("UPDATE musician SET instrument = '" + newInstrument + "', band =  '" + newBand +
        #     "'WHERE band = '" + oldBand + "'")
        #    self.conn.commit()
        # except Exception as e:
         #   print(e)
    
    ### Complex/Interesting Queries ###
    
    def sqlTopTenSongs(self):
        self.cur.execute(
            "SELECT song.title, rating.averageRating FROM song JOIN rating ON rating.songId = song.songId ORDER BY rating.averageRating DESC LIMIT 10")
        return self.getItems()

    # works
    def sqlTopTenAlbums(self):
        self.cur.execute(
            "SELECT album.title, rating.averageRating FROM album JOIN rating ON rating.albumId = album.albumId ORDER BY rating.averageRating DESC LIMIT 10")
        return self.getItems()

    # works - Complex Queries Series
    def findArtistBySongName(self, songName):
        try:
            self.cur.execute("SELECT A.artistName FROM Artist A, Contains C, Song S, Played P, Musician M WHERE S.title = '%s' AND S.songId = C.songId AND C.albumId = P.albumId AND P.musicianId = M.musicianId AND M.artistId = A.artistId" % (songName))
            return self.getItems()
        except Exception as e:
            print(e)

     # works - Complex Queries Series
    def tenMusicWithWorstRating(self):
        try:
            self.cur.execute(
                "SELECT song.title, rating.averageRating FROM song JOIN rating ON rating.songId = song.songId ORDER BY rating.averageRating ASC LIMIT 10")
            return self.getItems()
        except Exception as e:
            print(e)

    # works - Complex Queries Series
    def findSongNameWithYearByArtist(self, artistName, releaseYear):
        try:
            self.cur.execute("SELECT S.title, S.releaseYear FROM Artist A, Contains C, Song S, Played P, Musician M WHERE S.releaseYear >= %i AND A.artistName = '%s' AND S.songId = C.songId AND C.albumId = P.albumId AND P.musicianId = M.musicianId AND M.artistId = A.artistId" % (releaseYear, artistName))
            return self.getItems()
        except Exception as e:
            print(e)

    # works
    def findcompanyNameByAlbumName(self, albumName):
        try:
            self.cur.execute(
                "SELECT R.companyName FROM recordLabel R, publishes P, album A WHERE A.albumID = P.albumID AND P.recordLabelID = R.recordLabelID AND A.title = '%s'" % (albumName))
            return self.getItems()
        except Exception as e:
            print(e)

    # works
    def findLocationByAlbumName(self, albumName):
        try:
            self.cur.execute(
                "SELECT R.labelLocation FROM recordLabel R, publishes P, album A WHERE A.albumID = P.albumID AND P.recordLabelID = R.recordLabelID AND A.title = '%s'" % (albumName))
            return self.getItems()
        except Exception as e:
            print(e)

    # works
    def findRecLebDateByAlbumName(self, albumName):
        try:
            self.cur.execute(
                "SELECT R.dateEstablished FROM recordLabel R, publishes P, album A WHERE A.albumID = P.albumID AND P.recordLabelID = R.recordLabelID AND A.title = '%s'" % (albumName))
            return self.getItems()
        except Exception as e:
            print(e)

    # works
    def findcompanyNameBySongName(self, songName):
        try:
            self.cur.execute("SELECT R.companyName FROM recordLabel R, publishes P, album A, Contains C, Song S WHERE S.songID = C.songID AND C.albumID = A.albumID AND A.albumID = P.albumID AND P.recordLabelID = R.recordLabelID AND S.title = '%s'" % (songName))
            return self.getItems()
        except Exception as e:
            print(e)

    # works
    def findcompanyNameByBandName(self, bandName):
        try:
            self.cur.execute("SELECT R.companyName FROM musician M, played P1, publishes P2, recordLabel R WHERE M.musicianId = P1.musicianId AND P1.albumId = P2.albumId AND P2.recordLabelId = R.recordLabelId AND M.band = '%s'" % (bandName))
            return self.getItems()
        except Exception as e:
            print(e)
    # works

    def findListOfCompanyNameByInstrument(self, instName):
        try:
            self.cur.execute("SELECT R.companyName FROM musician M, played P1, publishes P2, recordLabel R WHERE M.musicianId = P1.musicianId AND P1.albumId = P2.albumId AND P2.recordLabelId = R.recordLabelId AND M.instrument = '%s'" % (instName))
            return self.getItems()
        except Exception as e:
            print(e)


    def insertNewSongToExistingsAlbumName(self, albumName, title, genre, releaseYear):
        songDuration = randint(30, 1000)
        userRating = 0
        songId = int(round(time.time()))
        sourceLink = fake.domain_name()
        averageRating = randint(10, 50)/10
        numOfRating = int(randint(1, 100000))
        try:
            self.cur.execute("SELECT albumId FROM album WHERE title = '%s'" % (albumName))
            albumId = self.getItems()[0][0]
            self.cur.execute("INSERT INTO song(title, genre, songDuration, songId, sourceLink, releaseYear) VALUES('%s', '%s', %i, %i,'%s', %i)" % (
                title, genre, songDuration, songId, sourceLink, releaseYear))
            self.cur.execute(
                "INSERT INTO contains(albumId, songId) VALUES( %i, %i)" % (albumId, songId))
            self.cur.execute("INSERT INTO rating(numOfRating, averageRating, userRating, albumId, songId ) VALUES( %i, %i, %i, %i, %i)" % (
                numOfRating, averageRating, userRating, albumId, songId))
        except Exception as e:
            print(e)

    def moveSongsBetweenAlbum(self, albumTitle, songTitle, genre, releaseYear):
            try:
                self.cur.execute("SELECT songId FROM song WHERE title = '%s' AND genre = '%s' AND releaseYear = '%s'" % (songTitle, genre, releaseYear))
                songId = self.getItems()[0][0]
                self.cur.execute("SELECT albumId FROM album WHERE title = '%s'" % (albumTitle))
                albumId = self.getItems()[0][0]
                self.cur.execute("INSERT INTO contains(albumId, songId) VALUES( %i, %i)" % (albumId, songId))
            except Exception as e:
                print(e)


# todo rate a song


# todo list all songs/albums from an artist

#
