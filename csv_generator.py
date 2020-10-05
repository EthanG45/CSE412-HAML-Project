# Team HAML

from faker import Faker 
import json    
import random
from random import randint

# import sys
# !{sys.executable} -m pip install Faker

Faker.seed(2)
fake = Faker() 

ins = ["Guitar", "Kazoo", "Piano", "Violin", "Viola", "Didgeridoo", "Drums", "Tambourines", "Hurdy Gurdy"]
genre = ["Rap", "Rock", "Country", "Hip Hop", "Soundtrack", "EDM", "Metal", "Heavy Metal", "Pop"]

music ={} 
for i in range(0, 1000): 
    num = i + 1
    music[i]={} 
    music[i]['companyName']= fake.color_name()
    music[i]['dateEstablished']= fake.date() 
    music[i]['location']= fake.city() 
    music[i]['recordLableId']= num 
    music[i]['albumId']= num
    music[i]['numOfRating']= randint(1,100000) 
    music[i]['averageRating']= randint(10, 50)/10
    music[i]['userRating']= 0
    music[i]['songId']= num
    music[i]['artistId']= num
    music[i]['name']= fake.name()
    music[i]['age']= randint(18, 70)
    music[i]['musicianId']= num
    music[i]['instrument']= random.choice(ins)
    music[i]['band']= fake.color_name() + " " + fake.word()
    music[i]['albumDuration']= randint(100, 10000)
    music[i]['albumTitle']= fake.word() + " " + fake.word() + " " + fake.word()
    music[i]['coverURL']= fake.image_url()
    music[i]['genre']= random.choice(genre)
    music[i]['songDuration']= randint(30, 1000)
    music[i]['songTitle']= fake.word() + " " + fake.word()
    music[i]['sourceLink']= fake.domain_name()
    music[i]['year']= fake.year()
    music[i]['knownFor']= fake.word() + " " + fake.word()

# print(music) 
# print(help(fake))

with open('Music.csv', 'w') as f:
     for key in music.keys():
            f.write("%s,%s\n"%(key,music[key]))
f.close() 

with open('RecordLabel.csv', 'w') as f1:
     for key,value in music.items():
            f1.write("%i,%s,%s,%s,%i\n"%(key,value['companyName'], value['dateEstablished'],value['location'],value['recordLableId']))    
f1.close()

with open('Publishes.csv', 'w') as f2:
     for key,value in music.items():
            f2.write("%i,%i,%i\n"%(key,value['albumId'], value['recordLableId']))    
f2.close()

with open('Rating.csv', 'w') as f3:
     for key,value in music.items():
            f3.write("%i,%f,%f,%i,%i,%i\n"%(key,value['numOfRating'], value['averageRating'],value['userRating'],value['albumId'], value['songId']))    
f3.close()


with open('Artist.csv', 'w') as f4:
     for key,value in music.items():
            f4.write("%i,%i,%s,%i\n"%(key,value['artistId'], value['name'], value['age']))    
f4.close()

with open('Musician.csv', 'w') as f5:
     for key,value in music.items():
            f5.write("%i,%i,%i,%s,%s\n"%(key,value['artistId'], value['musicianId'], value['instrument'], value['band']))    
f5.close()


with open('Played.csv', 'w') as f6:
     for key,value in music.items():
            f6.write("%i,%i,%i\n"%(key,value['albumId'], value['musicianId']))    
f6.close()


with open('Album.csv', 'w') as f7:
     for key,value in music.items():
            f7.write("%i,%i,%i,%s,%s\n"%(key,value['albumDuration'],value['albumId'],value['albumTitle'],value['coverURL']))    
f7.close()


with open('Song.csv', 'w') as f8:
     for key,value in music.items():
            f8.write("%i,%s,%s,%i,%i,%s,%s\n"%(key,value['songTitle'],value['genre'], value['songDuration'],value['songId'],value['sourceLink'],value['year']))    
f8.close()

with open('Contains.csv', 'w') as f9:
     for key,value in music.items():
            f9.write("%i,%i,%i\n"%(key,value['albumId'], value['songId']))    
f9.close()

with open('Made.csv', 'w') as f10:
     for key,value in music.items():
            f10.write("%i,%s,%i,%i\n"%(key,value['knownFor'],value['albumId'],value['artistId']))    
f10.close()



print("File Generation Completed!")