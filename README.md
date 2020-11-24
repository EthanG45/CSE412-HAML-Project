# 1. H.A.M.L. User Manual (CSE 412 Group Project)


<p align="center">
<img src="./image/HAML.png" alt="drawing" width="200"/>
</p>


- [1. H.A.M.L. User Manual (CSE 412 Group Project)](#1-haml-user-manual-cse-412-group-project)
  - [1.1. Main Screen](#11-main-screen)
  - [1.2. 1.2 Library](#12-12-library)
    - [1.2.1. `Song Library`](#121-song-library)
    - [1.2.2. `Album Library`](#122-album-library)
    - [1.2.3. `Artist Library`](#123-artist-library)
    - [1.2.4. `Record Label Library`](#124-record-label-library)
  - [1.3. Add](#13-add)
    - [1.3.1. `Add Song`](#131-add-song)
    - [1.3.2. `Add Album`](#132-add-album)
    - [1.3.3. `Add Artist`](#133-add-artist)
    - [1.3.4. 1.3.4 `Add Record Label`](#134-134-add-record-label)
  - [1.4. Search](#14-search)
    - [1.4.1. `Search Song`](#141-search-song)
    - [1.4.2. `Search Album`](#142-search-album)
    - [1.4.3. `Search Artist`](#143-search-artist)
    - [1.4.4. `Search Band`](#144-search-band)
    - [1.4.5. `Search Record Label`](#145-search-record-label)
  - [1.5. Insights](#15-insights)
    - [1.5.1. `Top 10 Songs`](#151-top-10-songs)
    - [1.5.2. `Graph Genre Song By User Rating`](#152-graph-genre-song-by-user-rating)
    - [1.5.3. `Top 10 Albums`](#153-top-10-albums)
    - [1.5.4. `Top 10 Worst Songs`](#154-top-10-worst-songs)
    - [1.5.5. `Top 10 Worst Albums`](#155-top-10-worst-albums)
  - [1.6. Feeling Lucky](#16-feeling-lucky)
    - [1.6.1. `Artists`](#161-artists)
    - [1.6.2. `Songs`](#162-songs)
    - [1.6.3. `Record Label by Album`](#163-record-label-by-album)
    - [1.6.4. `Record Label by Song`](#164-record-label-by-song)
    - [1.6.5. `Record Label by Band`](#165-record-label-by-band)
    - [1.6.6. `Record Label by Instrument`](#166-record-label-by-instrument)
  - [1.7. Theme](#17-theme)
    - [1.7.1. `Theme`](#171-theme)
  - [1.8. Contribution](#18-contribution)

## 1.1. Main Screen
HAML has 5 main tabs. They are:
1. Library
2. Add
3. Search
4. Insights
6. Feeling Lucky
7. Theme

![Theme](image/Theme.png?raw=true "Theme")

## 1.2. 1.2 Library
Library is a group of tabs:
1. Song
2. Album
3. Artist
4. Record Label


### 1.2.1. `Song Library`
Displays all songs from the song table in our database. It allows a user to select a table element and either update, delete or rate a song using a slider.

![Library Song](image/Library-Song.png?raw=true "Library Song")
![Update Song](image/Update-Song.png?raw=true "Update Song")
### 1.2.2. `Album Library`
Displays all albums from the album table in our database. It allows a user to select a table element and either update or delete an album.

![Library Album](image/Library-Album.png?raw=true "Library Album")
![Update Album](image/Update-Album.png?raw=true "Update Album")


### 1.2.3. `Artist Library`
Displays all artists from the artist table in our database. It allows a user to select a table element and either update or delete an artist. 

![Library Artist](image/Library-Artist.png?raw=true "Library Artist")
![Update Artist](image/Update-Artist.png?raw=true "Update Artist")

### 1.2.4. `Record Label Library`
Displays all record labels from the record label table in our database. It allows a user to select a table element and either update or delete a record label.

![Library Record Label](image/Library-Record-Label.png?raw=true "Library Record Label")
![Update Record Label](image/Update-Record-Label.png?raw=true "Update Record Label")

## 1.3. Add
Add is a group of tabs:
1. Song
2. Album
3. Artist
4. Record Label
  
### 1.3.1. `Add Song`
Add song allows a user to input a song title, genre, album title and release year. The release year uses a drop down menu for selection. 

![Add Song](image/Add-Song.png?raw=true "Add Song")
### 1.3.2. `Add Album`
Add album allows a user to input an album title and include the first song, which will contain the same elements as the add song function.

![Add Album](image/Add-Album.png?raw=true "Add Album")
### 1.3.3. `Add Artist`
Add artist allows a user to input an artist name, age, which uses a slider, instrument, which uses a list box, and band name. It then 
asks what album the artist makes and requires the user to add an album using the same parameters from add album.

![Add-Artist](image/Add-Artist.png?raw=true "Add Artist")
### 1.3.4. 1.3.4 `Add Record Label`
Add record label allows a user to input a company name, label location, and what album the record label published and asks for the title
using a list box. It also asks for the date established, which is entered using a calendar GUI, or you can manually enter the data in the
format YYYY-MM-DD. 

![Add Record Label](image/Add-Record-Label.png?raw=true "Add Record Label")


## 1.4. Search
Search is a tab group that contains tabs:
1. Song
2. Album
3. Artist
4. Band
5. Record Label

### 1.4.1. `Search Song`
Asks the user for the song name and has a button called search and once pressed, will fill a table with all of the returned results with
respect to the song name. There is also a rating slider to add a rating to the song and a delete button to delete the song and an update
button that can be used to update the song details.
![Search Song](image/Search-Song.png?raw=true "Search Song")

### 1.4.2. `Search Album`
Asks the user for the album title and has a button called search and once pressed, will fill a table with all of the returned results with 
respect to the album title. There are also delete and update buttons to delete the album and to update the album details.
![Search Album](image/Search-Album.png?raw=true "Search Album")

### 1.4.3. `Search Artist`
Asks the user for the artist name and has a button called search and once pressed, will fill a table with all of the returned results with 
respect to the artist title. There are also delete and update buttons to delete the artist and to update the artist details.
![Search Artist](image/Search-Artist.png?raw=true "Search Artist")

### 1.4.4. `Search Band`
Asks the user for the band name and has a button called search and once pressed, will fill a table with all of the returned results with 
respect to the band name. There are also delete and update buttons to delete the band and to update the band details.
![Search Band](image/Search-Band.png?raw=true "Search Band")

### 1.4.5. `Search Record Label`
Asks the user for the record label name and has a button called search and once pressed, will fill a table with all of the returned results with 
respect to the record label name. There are also delete and update buttons to delete the record label and to update the record label details.
![Search Record Label](image/Search-Record-Label.png?raw=true "Search Record Label")

## 1.5. Insights
Insights is a Group of Tabs:
1. Top 10 Songs
2. Genre Graph Song By User Rating
3. Top 10 Albums
4. Top 10 Worst Songs
5. Top 10 Worst Albums

### 1.5.1. `Top 10 Songs`
Display the top 10 songs in the database by overall average rating in one table and by user rating in another table.

![Insights Top Song Graph](image/Insights-Top-Song-Graph.png?raw=true "Insights Top Song Graph")
![Insights Top Song](image/Insights-Top-Song.png?raw=true "Insights Top Song")

### 1.5.2. `Graph Genre Song By User Rating`
Displays a distribution of genres by user rating.
### 1.5.3. `Top 10 Albums`
Display the top 10 albums in the database by overall average rating in one table and by user rating in another table.

![Insights Top Album](image/Insights-Top-Album.png?raw=true "Insights Top Album")
![Insights Top Album Graph](image/Insights-Top-Album-Graph.png?raw=true "Insights Top Album Graph")

### 1.5.4. `Top 10 Worst Songs`
Display the top 10 worst songs in the database by overall average rating in one table and by user rating in another table.

![Insights Worst Song Graph](image/Insights-Worst-Song-Graph.png?raw=true "Insights Worst Song Graph")
![Insights Worst Song](image/Insights-Worst-Song.png?raw=true "Insights Worst Song")

### 1.5.5. `Top 10 Worst Albums`
Display the top 10 worst albums in the database by overall average rating in one table and by user rating in another table.

![Insights Worst Album Graph](image/Insights-Worst-Album-Graph.png?raw=true "Insights Worst Album Graph")
![Insights Worst Album](image/Insights-Worst-Album.png?raw=true "Insights Worst Album")

## 1.6. Feeling Lucky
Feeling Lucky is a group of tabs:
1. Artists
2. Songs
3. Record Label by Album
4. Record Label by Song
5. Record Label by Band
6. Record Label by Instrument

### 1.6.1. `Artists`
Searches artist by song name and returns a table of artists by their song name.

![Feeling Lucky Artist](image/Feeling-Lucky-Artist.png?raw=true "Felling Lucky Artist")
### 1.6.2. `Songs`
Searches songs by year using a list box and artist using a drop down list and returns a table of information regarding the artists and songs entered.

![Feeling Lucky Song](image/Feeling-Lucky-Song.png?raw=true "Feeling Lucky Song")

### 1.6.3. `Record Label by Album`
Searches record label details by album. It uses a list box filled with all the album names for user selection.

![Feeling Lucky Record 1](image/Feeling-Lucky-Record-1.png?raw=true "Feeling Lucky Record 1")

### 1.6.4. `Record Label by Song`
Searches record label details by song. It uses a list box filled with all the song names for user selection.

![Feeling Lucky Record 2](image/Feeling-Lucky-Record-2.png?raw=true "Feeling Lucky Record 2")

### 1.6.5. `Record Label by Band`
Searches record label details by band. It uses a list box filled with all the band names for user selection.

![Feeling Lucky Record 3](image/Feeling-Lucky-Record-3.png?raw=true "Feeling Lucky Record 3")

### 1.6.6. `Record Label by Instrument`
Searches record label details by instrument. It uses a list box filled with all the instrument names for user selection.

![Feeling Lucky Record 4](image/Feeling-Lucky-Record-4.png?raw=true "Feeling Lucky Record 4")


## 1.7. Theme
### 1.7.1. `Theme`
Allows the user to select a theme from a list box and will change the graphical theme to match the theme selected.

  ![Theme](image/Theme.png?raw=true "Theme")

## 1.8. Contribution
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
  * Helped with some of the SQL functions.
* Jonathan Monk
  * Wrote and helped on a lot of SQL functions.
  * Made edits to the GUI.

* Ramón Deniz
  * Wrote custom GUI windows and components
  * Debugged main issues revolving around the GUI


