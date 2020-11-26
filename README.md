# 1. H.A.M.L. User Manual (CSE 412 Group Project)

<p align="center">
<img src="./image/HAML.png" alt="drawing" width="200"/>
</p>


- [1. H.A.M.L. User Manual (CSE 412 Group Project)](#1-haml-user-manual-cse-412-group-project)
  - [1.1. Setup](#11-setup)
    - [1.1.1. Step 1 - Python Dependencies](#111-step-1---python-dependencies)
    - [1.1.2. Step 2 - PostgreSQL setup](#112-step-2---postgresql-setup)
    - [1.1.3. Step 3 - Database setup](#113-step-3---database-setup)
    - [1.1.4. Step 4 - Run the app](#114-step-4---run-the-app)
    - [1.1.5. Already have the app setup?](#115-already-have-the-app-setup)
    - [1.1.6. Done with H.A.M.L.?](#116-done-with-haml)
  - [1.2. Main Screen](#12-main-screen)
  - [1.3. 1.2 Library](#13-12-library)
    - [1.3.1. `Song Library`](#131-song-library)
    - [1.3.2. `Album Library`](#132-album-library)
    - [1.3.3. `Artist Library`](#133-artist-library)
    - [1.3.4. `Record Label Library`](#134-record-label-library)
  - [1.4. Add](#14-add)
    - [1.4.1. `Add Song`](#141-add-song)
    - [1.4.2. `Add Album`](#142-add-album)
    - [1.4.3. `Add Artist`](#143-add-artist)
    - [1.4.4. 1.3.4 `Add Record Label`](#144-134-add-record-label)
  - [1.5. Search](#15-search)
    - [1.5.1. `Search Song`](#151-search-song)
    - [1.5.2. `Search Album`](#152-search-album)
    - [1.5.3. `Search Artist`](#153-search-artist)
    - [1.5.4. `Search Band`](#154-search-band)
    - [1.5.5. `Search Record Label`](#155-search-record-label)
  - [1.6. Insights](#16-insights)
    - [1.6.1. `Top 10 Songs`](#161-top-10-songs)
    - [1.6.2. `Graph Genre Song By User Rating`](#162-graph-genre-song-by-user-rating)
    - [1.6.3. `Top 10 Albums`](#163-top-10-albums)
    - [1.6.4. `Top 10 Worst Songs`](#164-top-10-worst-songs)
    - [1.6.5. `Top 10 Worst Albums`](#165-top-10-worst-albums)
  - [1.7. Feeling Lucky](#17-feeling-lucky)
    - [1.7.1. `Artists`](#171-artists)
    - [1.7.2. `Songs`](#172-songs)
    - [1.7.3. `Record Label by Album`](#173-record-label-by-album)
    - [1.7.4. `Record Label by Song`](#174-record-label-by-song)
    - [1.7.5. `Record Label by Band`](#175-record-label-by-band)
    - [1.7.6. `Record Label by Instrument`](#176-record-label-by-instrument)
  - [1.8. Theme](#18-theme)
    - [1.8.1. `Theme`](#181-theme)
  - [1.9. Contribution](#19-contribution)
  - [1.10. Developed using PySimpleGUI](#110-developed-using-pysimplegui)
  - [1.11. Known Bugs](#111-known-bugs)
  - [1.12. Repository Scripts](#112-repository-scripts)
    - [1.12.1. `./scripts/clean_db.sh`](#1121-scriptsclean_dbsh)
    - [1.12.2. `./scripts/demo.sh`](#1122-scriptsdemosh)
    - [1.12.3. `./scripts/enter_db.sh`](#1123-scriptsenter_dbsh)
    - [1.12.4. `./scripts/init_db.sh`](#1124-scriptsinit_dbsh)
    - [1.12.5. `python scripts/install.py`](#1125-python-scriptsinstallpy)
    - [1.12.6. `./scripts/refresh_db.sh`](#1126-scriptsrefresh_dbsh)
    - [1.12.7. `./scripts/rm_db.sh`](#1127-scriptsrm_dbsh)
    - [1.12.8. `./scripts/start_db.sh`](#1128-scriptsstart_dbsh)
    - [1.12.9. `./scripts/stop_db.sh`](#1129-scriptsstop_dbsh)
  - [1.13. Postgres Setup](#113-postgres-setup)
    - [1.13.1. `python3 postgres-setup/csv_generator.py`](#1131-python3-postgres-setupcsv_generatorpy)
  - [1.14. How does the database work / where is the raw database?](#114-how-does-the-database-work--where-is-the-raw-database)
  - [1.15. Video Demo of App](#115-video-demo-of-app)

## 1.1. Setup
**H.A.M.L. is supported on Linux and macOS, it does not support windows.**

[Interested in what the other shellscripts do?](#112-repository-scripts)

In order to get started clone this repository:

```zsh
git clone https://github.com/EthanG45/CSE412-HAML-Project.git
```

### 1.1.1. Step 1 - Python Dependencies
**H.A.M.L. requires python3 and pip**

**H.A.M.L. requires the following Python dependencies:**
1. PySimpleGUI
2. matplotlib
3. faker
4. psycopg2
5. psycopg2-binary

If you are on Linux, you need to install the following package:
```zsh
sudo apt-get install python3-tk
```

If you are on macOS, you need to install the following package with homebrew (also get [homebrew](https://brew.sh) if you don't have it). You also have to recompile Python with tcl-tk headers:
```zsh
brew install tcl-tk
```

Note we are assuming you are using [pyenv](https://github.com/pyenv/pyenv) for recompiling Python.

```zsh
latestTclTk='8.6'

latestPython=`pyenv install --list | sed -e 's/^[[:space:]]*//' | grep --regexp '^[0-9]\.[0-9][\.0-9]*$' | (gsort --version-sort 2>/dev/null || sort --version-sort) | tail -n 1`

PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I/usr/local/opt/tcl-tk/include' --with-tcltk-libs='-L/usr/local/opt/tcl-tk/lib -ltcl${latestTclTk} -ltk${latestTclTk}'"

pyenv install ${latestPython}

pyenv global ${latestPython}
```

Reference for this [tcl-tk issue on macOS](https://thad.getterman.org/articles/pysimplegui-and-tkinter-in-pyenv-with-homebrew/).

To download all the dependencies, simply run `scripts/install.py` using the command:
```zsh
python3 scripts/install.py
```

### 1.1.2. Step 2 - PostgreSQL setup
H.A.M.L. relies on your machine having [PostgreSQL](https://www.postgresql.org). Follow their [setup process](https://www.postgresql.org/download/) to get it.

The following exports are expected in your terminal for the duration of using H.A.M.L.

```zsh
export PATH="/Library/PostgreSQL/12/bin:${PATH}" # mac
export PATH="/usr/lib/postgresql/12/bin:${PATH}" # linux
```

```zsh
export PGPORT=8888   # e.g. 8888. It sets the PORT to be this number 8888 which will be used by PostgreSQL
export PGHOST=/tmp    # sets the directory for the socket files
```

If you intend to use H.A.M.L. in more than one terminal session, then add the exports to your .bashrc or .zshrc. If not, then make sure to run the exports each time you use H.A.M.L. in your terminal.

### 1.1.3. Step 3 - Database setup

Run the `./scripts/init_db.sh` command. This will setup the H.A.M.L. database on your machine. It must be run from the root directory.

```zsh
./scripts/init_db.sh
```

### 1.1.4. Step 4 - Run the app
Run the app using the following `gui.py` file:

```zsh
python3 src/gui.py
```

### 1.1.5. Already have the app setup?

Just run `./scripts/start_db.sh` to start the database and `./scripts/stop_db.sh` to stop it when you are done using the app.

```zsh
./scripts/start_db.sh
./scripts/stop_db.sh
```
### 1.1.6. Done with H.A.M.L.?

Just run `./scripts/rm_db.sh` to remove the database and delete this repository.

```zsh
./scripts/rm_db.sh
```

## 1.2. Main Screen
HAML has 5 main tabs. They are:
1. Library
2. Add
3. Search
4. Insights
6. Feeling Lucky
7. Theme

![Theme](image/Theme.png?raw=true "Theme")

## 1.3. 1.2 Library
Library is a group of tabs:
1. Song
2. Album
3. Artist
4. Record Label


### 1.3.1. `Song Library`
Displays all songs from the song table in our database. It allows a user to select a table element and either update, delete or rate a song using a slider.

![Library Song](image/Library-Song.png?raw=true "Library Song")
![Update Song](image/Update-Song.png?raw=true "Update Song")
### 1.3.2. `Album Library`
Displays all albums from the album table in our database. It allows a user to select a table element and either update or delete an album.

![Library Album](image/Library-Album.png?raw=true "Library Album")
![Update Album](image/Update-Album.png?raw=true "Update Album")


### 1.3.3. `Artist Library`
Displays all artists from the artist table in our database. It allows a user to select a table element and either update or delete an artist. 

![Library Artist](image/Library-Artist.png?raw=true "Library Artist")
![Update Artist](image/Update-Artist.png?raw=true "Update Artist")

### 1.3.4. `Record Label Library`
Displays all record labels from the record label table in our database. It allows a user to select a table element and either update or delete a record label.

![Library Record Label](image/Library-Record-Label.png?raw=true "Library Record Label")
![Update Record Label](image/Update-Record-Label.png?raw=true "Update Record Label")

## 1.4. Add
Add is a group of tabs:
1. Song
2. Album
3. Artist
4. Record Label
  
### 1.4.1. `Add Song`
Add song allows a user to input a song title, genre, album title and release year. The release year uses a drop down menu for selection. 

![Add Song](image/Add-Song.png?raw=true "Add Song")
### 1.4.2. `Add Album`
Add album allows a user to input an album title and include the first song, which will contain the same elements as the add song function.

![Add Album](image/Add-Album.png?raw=true "Add Album")
### 1.4.3. `Add Artist`
Add artist allows a user to input an artist name, age, which uses a slider, instrument, which uses a list box, and band name. It then 
asks what album the artist makes and requires the user to add an album using the same parameters from add album.

![Add-Artist](image/Add-Artist.png?raw=true "Add Artist")
### 1.4.4. 1.3.4 `Add Record Label`
Add record label allows a user to input a company name, label location, and what album the record label published and asks for the title
using a list box. It also asks for the date established, which is entered using a calendar GUI, or you can manually enter the data in the
format YYYY-MM-DD. 

![Add Record Label](image/Add-Record-Label.png?raw=true "Add Record Label")


## 1.5. Search
Search is a tab group that contains tabs:
1. Song
2. Album
3. Artist
4. Band
5. Record Label

### 1.5.1. `Search Song`
Asks the user for the song name and has a button called search and once pressed, will fill a table with all of the returned results with
respect to the song name. There is also a rating slider to add a rating to the song and a delete button to delete the song and an update
button that can be used to update the song details.
![Search Song](image/Search-Song.png?raw=true "Search Song")

### 1.5.2. `Search Album`
Asks the user for the album title and has a button called search and once pressed, will fill a table with all of the returned results with 
respect to the album title. There are also delete and update buttons to delete the album and to update the album details.
![Search Album](image/Search-Album.png?raw=true "Search Album")

### 1.5.3. `Search Artist`
Asks the user for the artist name and has a button called search and once pressed, will fill a table with all of the returned results with 
respect to the artist title. There are also delete and update buttons to delete the artist and to update the artist details.
![Search Artist](image/Search-Artist.png?raw=true "Search Artist")

### 1.5.4. `Search Band`
Asks the user for the band name and has a button called search and once pressed, will fill a table with all of the returned results with 
respect to the band name. There are also delete and update buttons to delete the band and to update the band details.
![Search Band](image/Search-Band.png?raw=true "Search Band")

### 1.5.5. `Search Record Label`
Asks the user for the record label name and has a button called search and once pressed, will fill a table with all of the returned results with 
respect to the record label name. There are also delete and update buttons to delete the record label and to update the record label details.
![Search Record Label](image/Search-Record-Label.png?raw=true "Search Record Label")

## 1.6. Insights
Insights is a Group of Tabs:
1. Top 10 Songs
2. Genre Graph Song By User Rating
3. Top 10 Albums
4. Top 10 Worst Songs
5. Top 10 Worst Albums

### 1.6.1. `Top 10 Songs`
Display the top 10 songs in the database by overall average rating in one table and by user rating in another table.

![Insights Top Song Graph](image/Insights-Top-Song-Graph.png?raw=true "Insights Top Song Graph")
![Insights Top Song](image/Insights-Top-Song.png?raw=true "Insights Top Song")

### 1.6.2. `Graph Genre Song By User Rating`
Displays a distribution of genres by user rating.
### 1.6.3. `Top 10 Albums`
Display the top 10 albums in the database by overall average rating in one table and by user rating in another table.

![Insights Top Album](image/Insights-Top-Album.png?raw=true "Insights Top Album")
![Insights Top Album Graph](image/Insights-Top-Album-Graph.png?raw=true "Insights Top Album Graph")

### 1.6.4. `Top 10 Worst Songs`
Display the top 10 worst songs in the database by overall average rating in one table and by user rating in another table.

![Insights Worst Song Graph](image/Insights-Worst-Song-Graph.png?raw=true "Insights Worst Song Graph")
![Insights Worst Song](image/Insights-Worst-Song.png?raw=true "Insights Worst Song")

### 1.6.5. `Top 10 Worst Albums`
Display the top 10 worst albums in the database by overall average rating in one table and by user rating in another table.

![Insights Worst Album Graph](image/Insights-Worst-Album-Graph.png?raw=true "Insights Worst Album Graph")
![Insights Worst Album](image/Insights-Worst-Album.png?raw=true "Insights Worst Album")

## 1.7. Feeling Lucky
Feeling Lucky is a group of tabs:
1. Artists
2. Songs
3. Record Label by Album
4. Record Label by Song
5. Record Label by Band
6. Record Label by Instrument

### 1.7.1. `Artists`
Searches artist by song name and returns a table of artists by their song name.

![Feeling Lucky Artist](image/Feeling-Lucky-Artist.png?raw=true "Felling Lucky Artist")
### 1.7.2. `Songs`
Searches songs by year using a list box and artist using a drop down list and returns a table of information regarding the artists and songs entered.

![Feeling Lucky Song](image/Feeling-Lucky-Song.png?raw=true "Feeling Lucky Song")

### 1.7.3. `Record Label by Album`
Searches record label details by album. It uses a list box filled with all the album names for user selection.

![Feeling Lucky Record 1](image/Feeling-Lucky-Record-1.png?raw=true "Feeling Lucky Record 1")

### 1.7.4. `Record Label by Song`
Searches record label details by song. It uses a list box filled with all the song names for user selection.

![Feeling Lucky Record 2](image/Feeling-Lucky-Record-2.png?raw=true "Feeling Lucky Record 2")

### 1.7.5. `Record Label by Band`
Searches record label details by band. It uses a list box filled with all the band names for user selection.

![Feeling Lucky Record 3](image/Feeling-Lucky-Record-3.png?raw=true "Feeling Lucky Record 3")

### 1.7.6. `Record Label by Instrument`
Searches record label details by instrument. It uses a list box filled with all the instrument names for user selection.

![Feeling Lucky Record 4](image/Feeling-Lucky-Record-4.png?raw=true "Feeling Lucky Record 4")


## 1.8. Theme
### 1.8.1. `Theme`
Allows the user to select a theme from a list box and will change the graphical theme to match the theme selected.

  ![Theme](image/Theme.png?raw=true "Theme")

## 1.9. Contribution
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

## 1.10. Developed using PySimpleGUI
  https://pypi.org/project/PySimpleGUI/

## 1.11. Known Bugs
1. Insights Graphs don't auto update. This is an issue inherent to the way PySimpleGUI and MatPlotLib are integrated with one another. It's very difficult to redraw the graphs without causing excessive CPU and memory load. We were unable to fix this within the scope of the project.
2. Focus Issues. The macOS version of PySimpleGUI currently has an issue where pop-up windows break the focus from the main window and prevent it from returning. There are some hacky fixes to this, but certain built-in elements can't be prevented from having this issue. One instance is the use of the built-in PySimpleGUI calendar in one of our addition tabs. It prevents focus from returning to the main app. This bug is not present on Linux.

## 1.12. Repository Scripts
### 1.12.1. `./scripts/clean_db.sh`
Drops the sql tables from your local version of the database.

```zsh
./scripts/clean_db.sh
```
### 1.12.2. `./scripts/demo.sh`
Runs a basic demo test of the database. Output is stored in the folder output

```zsh
./scripts/demo.sh
```

### 1.12.3. `./scripts/enter_db.sh`
Very lazy script that just enters you into the PostgreSQL command line.

```zsh
./scripts/enter_db.sh
```

### 1.12.4. `./scripts/init_db.sh`
Creates the H.A.M.L. database on your machine.

```zsh
./scripts/init_db.sh
```

### 1.12.5. `python scripts/install.py`
Downloads the necessary packages to your machine.

```zsh
python3 scripts/install.py
```

### 1.12.6. `./scripts/refresh_db.sh`
Refreshes the database by regenerating the PostgreSQL tables.
```zsh
./scripts/refresh_db.sh
```

### 1.12.7. `./scripts/rm_db.sh`
Remove databases entirely from your local machine.

```zsh
./scripts/rm_db.sh
```

### 1.12.8. `./scripts/start_db.sh`
Lazy script that starts the PostgreSQL database on your machine.

```zsh
./scripts/start_db.sh
```

### 1.12.9. `./scripts/stop_db.sh`
Lazy script that stops the PostgreSQL database on your machine.

```zsh
./scripts/stop_db.sh
```

## 1.13. Postgres Setup
### 1.13.1. `python3 postgres-setup/csv_generator.py`
This regenerates the database if you want to do that for some reason. The raw database is stored in the data folder.

## 1.14. How does the database work / where is the raw database?
The database is stored raw in the csv files under the [data folder](https://github.com/EthanG45/CSE412-HAML-Project/tree/main/data).

## 1.15. Video Demo of App
See a demo of the app [here](https://youtu.be/rwT69BiaMFo)

[![HAML Video](http://img.youtube.com/vi/rwT69BiaMFo/0.jpg)](http://www.youtube.com/watch?v=rwT69BiaMFo "HAML Video")
