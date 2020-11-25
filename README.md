# 1. H.A.M.L. User Manual (CSE 412 Group Project)
commands to use to start the database assuming 
all installs and paths are already set

./init_db.sh
./script/start_db.sh
python3 gui.py

# 2. copy pasta installs, Path additions, 
pip3 install PyPI
pip3 install PySimpleGUI
pip3 install matplotlib
pip3 install faker
pip3 install psycopg2
pip3 install psycopg2-binary

sudo apt-get install postgresql
sudo apt-get install postgresql-client
sudo apt-get install python3-psycopg2
sudo apt install postgresql postgresql-contrib

export PATH ="/Library/PostgreSQL/12/bin:${PATH}" # mac
export PATH ="/usr/lib/postgresql/12/bin:${PATH}" # linux

export PGPORT=8888
export PGHOST=/tmp

# 3. stuff U might need
pip3 install tk 
pip3 install Qt 
pip3 install Web 
pip3 install WxPython 
sudo apt-get install python3-tk
pip3 install pyinstaller 


<p align="center">
<img src="./image/HAML.png" alt="drawing" width="200"/>
</p>


- [1. H.A.M.L. User Manual (CSE 412 Group Project)](#1-haml-user-manual-cse-412-group-project)
- [2. copy pasta installs, Path additions,](#2-copy-pasta-installs-path-additions)
- [3. stuff U might need](#3-stuff-u-might-need)
  - [3.1. Main Screen](#31-main-screen)
  - [3.2. 1.2 Library](#32-12-library)
    - [3.2.1. `Song Library`](#321-song-library)
    - [3.2.2. `Album Library`](#322-album-library)
    - [3.2.3. `Artist Library`](#323-artist-library)
    - [3.2.4. `Record Label Library`](#324-record-label-library)
  - [3.3. Add](#33-add)
    - [3.3.1. `Add Song`](#331-add-song)
    - [3.3.2. `Add Album`](#332-add-album)
    - [3.3.3. `Add Artist`](#333-add-artist)
    - [3.3.4. 1.3.4 `Add Record Label`](#334-134-add-record-label)
  - [3.4. Search](#34-search)
    - [3.4.1. `Search Song`](#341-search-song)
    - [3.4.2. `Search Album`](#342-search-album)
    - [3.4.3. `Search Artist`](#343-search-artist)
    - [3.4.4. `Search Band`](#344-search-band)
    - [3.4.5. `Search Record Label`](#345-search-record-label)
  - [3.5. Insights](#35-insights)
    - [3.5.1. `Top 10 Songs`](#351-top-10-songs)
    - [3.5.2. `Graph Genre Song By User Rating`](#352-graph-genre-song-by-user-rating)
    - [3.5.3. `Top 10 Albums`](#353-top-10-albums)
    - [3.5.4. `Top 10 Worst Songs`](#354-top-10-worst-songs)
    - [3.5.5. `Top 10 Worst Albums`](#355-top-10-worst-albums)
  - [3.6. Feeling Lucky](#36-feeling-lucky)
    - [3.6.1. `Artists`](#361-artists)
    - [3.6.2. `Songs`](#362-songs)
    - [3.6.3. `Record Label by Album`](#363-record-label-by-album)
    - [3.6.4. `Record Label by Song`](#364-record-label-by-song)
    - [3.6.5. `Record Label by Band`](#365-record-label-by-band)
    - [3.6.6. `Record Label by Instrument`](#366-record-label-by-instrument)
  - [3.7. Theme](#37-theme)
    - [3.7.1. `Theme`](#371-theme)
  - [3.8. Contribution](#38-contribution)
  - [3.9. Developed using PySimpleGUI](#39-developed-using-pysimplegui)
  - [3.10. Known Bugs](#310-known-bugs)

## 3.1. Main Screen
HAML has 5 main tabs. They are:
1. Library
2. Add
3. Search
4. Insights
6. Feeling Lucky
7. Theme

![Theme](image/Theme.png?raw=true "Theme")

## 3.2. 1.2 Library
Library is a group of tabs:
1. Song
2. Album
3. Artist
4. Record Label


### 3.2.1. `Song Library`
Displays all songs from the song table in our database. It allows a user to select a table element and either update, delete or rate a song using a slider.

![Library Song](image/Library-Song.png?raw=true "Library Song")
![Update Song](image/Update-Song.png?raw=true "Update Song")
### 3.2.2. `Album Library`
Displays all albums from the album table in our database. It allows a user to select a table element and either update or delete an album.

![Library Album](image/Library-Album.png?raw=true "Library Album")
![Update Album](image/Update-Album.png?raw=true "Update Album")


### 3.2.3. `Artist Library`
Displays all artists from the artist table in our database. It allows a user to select a table element and either update or delete an artist. 

![Library Artist](image/Library-Artist.png?raw=true "Library Artist")
![Update Artist](image/Update-Artist.png?raw=true "Update Artist")

### 3.2.4. `Record Label Library`
Displays all record labels from the record label table in our database. It allows a user to select a table element and either update or delete a record label.

![Library Record Label](image/Library-Record-Label.png?raw=true "Library Record Label")
![Update Record Label](image/Update-Record-Label.png?raw=true "Update Record Label")

## 3.3. Add
Add is a group of tabs:
1. Song
2. Album
3. Artist
4. Record Label
  
### 3.3.1. `Add Song`
Add song allows a user to input a song title, genre, album title and release year. The release year uses a drop down menu for selection. 

![Add Song](image/Add-Song.png?raw=true "Add Song")
### 3.3.2. `Add Album`
Add album allows a user to input an album title and include the first song, which will contain the same elements as the add song function.

![Add Album](image/Add-Album.png?raw=true "Add Album")
### 3.3.3. `Add Artist`
Add artist allows a user to input an artist name, age, which uses a slider, instrument, which uses a list box, and band name. It then 
asks what album the artist makes and requires the user to add an album using the same parameters from add album.

![Add-Artist](image/Add-Artist.png?raw=true "Add Artist")
### 3.3.4. 1.3.4 `Add Record Label`
Add record label allows a user to input a company name, label location, and what album the record label published and asks for the title
using a list box. It also asks for the date established, which is entered using a calendar GUI, or you can manually enter the data in the
format YYYY-MM-DD. 

![Add Record Label](image/Add-Record-Label.png?raw=true "Add Record Label")


## 3.4. Search
Search is a tab group that contains tabs:
1. Song
2. Album
3. Artist
4. Band
5. Record Label

### 3.4.1. `Search Song`
Asks the user for the song name and has a button called search and once pressed, will fill a table with all of the returned results with
respect to the song name. There is also a rating slider to add a rating to the song and a delete button to delete the song and an update
button that can be used to update the song details.
![Search Song](image/Search-Song.png?raw=true "Search Song")

### 3.4.2. `Search Album`
Asks the user for the album title and has a button called search and once pressed, will fill a table with all of the returned results with 
respect to the album title. There are also delete and update buttons to delete the album and to update the album details.
![Search Album](image/Search-Album.png?raw=true "Search Album")

### 3.4.3. `Search Artist`
Asks the user for the artist name and has a button called search and once pressed, will fill a table with all of the returned results with 
respect to the artist title. There are also delete and update buttons to delete the artist and to update the artist details.
![Search Artist](image/Search-Artist.png?raw=true "Search Artist")

### 3.4.4. `Search Band`
Asks the user for the band name and has a button called search and once pressed, will fill a table with all of the returned results with 
respect to the band name. There are also delete and update buttons to delete the band and to update the band details.
![Search Band](image/Search-Band.png?raw=true "Search Band")

### 3.4.5. `Search Record Label`
Asks the user for the record label name and has a button called search and once pressed, will fill a table with all of the returned results with 
respect to the record label name. There are also delete and update buttons to delete the record label and to update the record label details.
![Search Record Label](image/Search-Record-Label.png?raw=true "Search Record Label")

## 3.5. Insights
Insights is a Group of Tabs:
1. Top 10 Songs
2. Genre Graph Song By User Rating
3. Top 10 Albums
4. Top 10 Worst Songs
5. Top 10 Worst Albums

### 3.5.1. `Top 10 Songs`
Display the top 10 songs in the database by overall average rating in one table and by user rating in another table.

![Insights Top Song Graph](image/Insights-Top-Song-Graph.png?raw=true "Insights Top Song Graph")
![Insights Top Song](image/Insights-Top-Song.png?raw=true "Insights Top Song")

### 3.5.2. `Graph Genre Song By User Rating`
Displays a distribution of genres by user rating.
### 3.5.3. `Top 10 Albums`
Display the top 10 albums in the database by overall average rating in one table and by user rating in another table.

![Insights Top Album](image/Insights-Top-Album.png?raw=true "Insights Top Album")
![Insights Top Album Graph](image/Insights-Top-Album-Graph.png?raw=true "Insights Top Album Graph")

### 3.5.4. `Top 10 Worst Songs`
Display the top 10 worst songs in the database by overall average rating in one table and by user rating in another table.

![Insights Worst Song Graph](image/Insights-Worst-Song-Graph.png?raw=true "Insights Worst Song Graph")
![Insights Worst Song](image/Insights-Worst-Song.png?raw=true "Insights Worst Song")

### 3.5.5. `Top 10 Worst Albums`
Display the top 10 worst albums in the database by overall average rating in one table and by user rating in another table.

![Insights Worst Album Graph](image/Insights-Worst-Album-Graph.png?raw=true "Insights Worst Album Graph")
![Insights Worst Album](image/Insights-Worst-Album.png?raw=true "Insights Worst Album")

## 3.6. Feeling Lucky
Feeling Lucky is a group of tabs:
1. Artists
2. Songs
3. Record Label by Album
4. Record Label by Song
5. Record Label by Band
6. Record Label by Instrument

### 3.6.1. `Artists`
Searches artist by song name and returns a table of artists by their song name.

![Feeling Lucky Artist](image/Feeling-Lucky-Artist.png?raw=true "Felling Lucky Artist")
### 3.6.2. `Songs`
Searches songs by year using a list box and artist using a drop down list and returns a table of information regarding the artists and songs entered.

![Feeling Lucky Song](image/Feeling-Lucky-Song.png?raw=true "Feeling Lucky Song")

### 3.6.3. `Record Label by Album`
Searches record label details by album. It uses a list box filled with all the album names for user selection.

![Feeling Lucky Record 1](image/Feeling-Lucky-Record-1.png?raw=true "Feeling Lucky Record 1")

### 3.6.4. `Record Label by Song`
Searches record label details by song. It uses a list box filled with all the song names for user selection.

![Feeling Lucky Record 2](image/Feeling-Lucky-Record-2.png?raw=true "Feeling Lucky Record 2")

### 3.6.5. `Record Label by Band`
Searches record label details by band. It uses a list box filled with all the band names for user selection.

![Feeling Lucky Record 3](image/Feeling-Lucky-Record-3.png?raw=true "Feeling Lucky Record 3")

### 3.6.6. `Record Label by Instrument`
Searches record label details by instrument. It uses a list box filled with all the instrument names for user selection.

![Feeling Lucky Record 4](image/Feeling-Lucky-Record-4.png?raw=true "Feeling Lucky Record 4")


## 3.7. Theme
### 3.7.1. `Theme`
Allows the user to select a theme from a list box and will change the graphical theme to match the theme selected.

  ![Theme](image/Theme.png?raw=true "Theme")

## 3.8. Contribution
Note on	 the commit history: the app was mostly programmed using VSCode LiveShare using Ethan's machine. This means the commit history shows only Ethan contributing code, but everyone did.

* General things everyone did roughly equally
  * Fixed bugs together (after introducing bugs).
  * Debug issues with the gui/sql, generally the ones they introduced sometimes just getting pulled in regardless to fix them even if they didn’t create them.
  * Documented features and what they generally worked on.
* Arvin Arasteh
  * Implemented the initial database connection to the program’s frontend and implemented most of the SQL queries and functions
  * Helped with the GUI’s different tabs,  and created different graphs for the program

* Aurelio Villalobos
  * Wrote SQL queries to interact with the GUI.
  * Wrote the user manual to explain how to use the program.
* Joshua Webber  
  * First to start the gui and implement most of the tabs not all features within each tab though, but still many aspects of them.
  * Edit the SQL functions for the implementation in the GUI
* Ethan Gilchrist
  * Worked on the GUI and a lot of the different tabs. Did most the work on the feeling lucky and insights tab. Helped on all other tabs.
  * Helped with some of the SQL functions. Made and edited the video.
* Jonathan Monk
  * Wrote and helped on a lot of SQL functions.
  * Made edits to the GUI.

* Ramón Deniz
  * Wrote custom GUI windows and components
  * Debugged main issues revolving around the GUI

## 3.9. Developed using PySimpleGUI
  https://pypi.org/project/PySimpleGUI/

## 3.10. Known Bugs
1. Insights Graphs don't auto update. This is an issue inherent to the way PySimpleGUI and MatPlotLib are integrated with one another. It's very difficult to redraw the graphs without causing excessive CPU and memory load. We were unable to fix this within the scope of the project.
2. Focus Issues. The macOS version of PySimpleGUI currently has an issue where pop-up windows break the focus from the main window and prevent it from returning. There are some hacky fixes to this, but certain built-in elements can't be prevented from having this issue. One instance is the use of the built-in PySimpleGUI calendar in one of our addition tabs. It prevents focus from returning to the main app. This bug is not present on Linux.