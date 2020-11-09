import getpass
import psycopg2
from string import Template
from psycopg2 import OperationalError

userName = getpass.getuser()

conn = psycopg2.connect(database=userName, user=userName,
                        host='/tmp', port='8888')
cur = conn.cursor()


# works
def getItems():
    result = []
    for i in cur:
        result.append(i)
    return result

# works
def sqlTopTenMusic():
    result = []
    cur.execute("SELECT song.title, rating.averageRating FROM song JOIN rating ON rating.songId = song.songId ORDER BY rating.averageRating DESC LIMIT 10")
    return getItems()

# Query - works
def sqlReadAny(query):
    cur.execute(query)
    return getItems()

# works
def updateSongSourceLink(title, genre, songId, newSourceLink, oldSourceLink ,releaseYear, songDuration):
    conn.set_session(autocommit=True)
    try:
        cur.execute("UPDATE song SET sourceLink= '" + newSourceLink +"'" + "WHERE song.title= '" + title + "'" + "AND songId= '" 
                        + str(songId) +"'" + "AND genre = '" + genre +"'" + "AND releaseYear= '" + str(releaseYear) + "'" 
                        + "AND songDuration= '" + str(songDuration) + "'" + "AND sourceLink= '" + oldSourceLink + "'")
        print('Updated: Replaced ', oldSourceLink, ' with ', newSourceLink)
    except Exception as e:
        print(e)

# works
def getAllSongs():
    result = []
    cur.execute("SELECT * FROM song")
    return getItems()

# works
def searchSong(songName):
    result = []
    try:
        cur.execute("SELECT * FROM song WHERE song.title = '%s'" % (songName))
        return getItems()
    except:
        return "Song not found"

def deleteSong(songName):
    try:
        cur.execute("DELETE FROM song WHERE song.title = '" +  songName + "'")
        return "Success! Song has been deleted. To show results, print all the songs"
    except:
        return "Error: The searched for song does not currently exist in the database"

# works
def insertRecordLabel(companyName, dateEstablished, labelLocation, recordLabelId):
    try:
        cur.execute("INSERT INTO recordLabel(companyName, dateEstablished, labelLocation, recordLabelId) VALUES( '" + companyName + "', '" + dateEstablished + "', '" + labelLocation + "', '" + str(recordLabelId) + "')")
    except Exception as e:
        print(e)

def deleteRecordLabel(companyName,dateEstablished, labelLocation, recordLabelId):
    try:
        cur.execute("DELETE FROM recordLabel WHERE recordLabelId= '" + str(recordLabelId) + "'" + "AND recordLabel.companyName= '" 
            + companyName + "'" + "AND dateEstablished= '" + dateEstablished + "'" + "AND recordLabel.labelLocation= '" + labelLocation + "'" )
        print("Deleted Row with ", recordLabelId)
    except Exception as e:
        print(e)

# insertRecordLabel("arvin","1973-11-06","ggbois",2005) #11/6/1973
# print(sqlReadAny("SELECT companyName, recordLabelId FROM recordLabel WHERE recordLabelId=2002"))

#printAllSongs()
# searchSong("top that")
#updateSongSourceLink('top that', 'EDM', 1, 'this.com', 'frederick-velez.com' ,2005, 615)
# print(sqlReadAny("SELECT * FROM recordLabel"))
# deleteRecordLabel('Arvin','1973-11-06','ggbois',2002)
# print(searchSong("top that"))

# todo add music

# todo edit existing music


# todo view music (search functionality)

# todo rate a song
def updateRate(rating,  songId):
    curr.execute("UPDATE song SET rating = " + rating + "WHERE songId = " + songId + ";")
    return getItems()  

# todo delete music

# todo list all songs/albums from an artist

# todo search albums


cur.close()
conn.close()
