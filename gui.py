# HAML_GUI

import PySimpleGUI as sg
import sql
# import tabs/create
from tabs.create import CreateTab
from tabs.delete import DeleteTab
from tabs.update import UpdateTab
from tabs.library import LibraryTab
from tabs.search import SearchTab

db = sql.Database()  # import db
ct = CreateTab(db)
dt = DeleteTab(db)
ut = UpdateTab(db)
lt = LibraryTab(db)
st = SearchTab(db)

events = []
st.addEvents(events)

sg.theme('Dark Grey 9')  # set window theme

# Define the window's contents


class GUI:
    def __init__(self):
        self.recordTable = db.getAllRecordLabels()
        self.artistTable = db.getAllArtists()
        self.albumsTable = db.getAllAlbums()
        self.songsTable = db.getAllSongs()
        self.songToLinkToAlbum = []
        self.createAlbumSongSearch = []

    def updateTables(self):
        self.recordTable = db.getAllRecordLabels()
        self.artistTable = db.getAllArtists()
        self.albumsTable = db.getAllAlbums()
        self.songsTable = db.getAllSongs()


def main():
    gui = GUI()

    # main layout this contains everything
    layout = [[
        sg.TabGroup(
            [[
                ct.createTabGUI(),
                ut.updateTabGUI(),
                dt.deleteTabGUI(),
                st.searchTabGUI(),
                lt.libraryTabGUI()
            ]],
            key='tabgroup',
            enable_events=True
        )  # end of TabGroup

    ]
    ]  # end of layout

    # Create the window
    window = sg.Window('H.A.M.L.', layout, font=(
        "Roboto", 12), size=(1280, 720), finalize=True)

    def isValid(*args):
        for elem in args:
            if elem == '':
                return False
        return True

    def updatelibtabs():
        gui.updateTables()
        window['-TABLE-L01-'].update(values=gui.recordTable)
        window['-TABLE-L02-'].update(values=gui.artistTable)
        window['-TABLE-L03-'].update(values=gui.albumsTable)
        window['-TABLE-L04-'].update(values=gui.songsTable)

    def checkButtonPress(event, values):

        ### SEARCH EVENTS ###

        if event == '-BUTTON-SEARCH-ARTIST-':
            temp = db.searchArtist(values['-INPUT-SEARCH-ARTIST-'])
            window['-TABLE-SEARCH-ARTIST-'].update(values=temp)

        if event == '-BUTTON-SEARCH-ALBUM-':
            temp = db.searchAlbum(values['-INPUT-SEARCH-ALBUM-'])
            window['-TABLE-SEARCH-ALBUM-'].update(values=temp)

        if event == '-BUTTON-SEARCH-MUSICIAN-':
            temp = db.searchMusician(values['-INPUT-SEARCH-MUSICIAN-'])
            window['-TABLE-SEARCH-MUSICIAN-'].update(values=temp)

        if event == '-BUTTON-SEARCH-RECORD-':
            temp = db.searchRecordLabel(values['-INPUT-SEARCH-RECORD-'])
            window['-TABLE-SEARCH-RECORD-'].update(values=temp)

        ### CREATE EVENTS ###

        # CREATE RECORD LABEL
        if event == '-BUTTON-C01-':
            companyName = values['-companyName-C01-']
            labelLocation = values['-labelLocation-C01-']
            dateEstablished = values['-dateEstablished-C01-']

            if isValid(companyName, dateEstablished, labelLocation):
                db.insertRecordLabel(
                    companyName, dateEstablished, labelLocation)
                #window['-TABLE-L01-'].update(values = db.getAllRecordLabels())
                window.FindElement('-companyName-C01-').update('')
                window.FindElement('-labelLocation-C01-').update('')
                window.FindElement('-dateEstablished-C01-').update('')
            else:
                window['-OUTPUT-C01-'].update("Failed to create Record Label!")

            # Force this window to have focus after window change (macos bug)
            window.TKroot.focus_force()
            updatelibtabs()

        # CREATE ARTIST
        if event == '-BUTTON-C02-':
            artistName = values['-ARTIST-C02-']
            artistAge = int(values['-AGE-C02-'])
            artistInstrument = values['-INSTRUMENT-C02-']
            artistBand = values['-BAND-C02-']
            titleName = values['-TITLE-C02-']

            if isValid(artistName, artistAge, artistInstrument, artistBand, titleName):
                db.insertArtist(artistName, artistAge,
                                artistInstrument, artistBand, titleName)
                window.FindElement('-ARTIST-C02-').update('')
                window.FindElement('-AGE-C02-').update('')
                window.FindElement('-INSTRUMENT-C02-').update('')
                window.FindElement('-BAND-C02-').update('')
                window.FindElement('-TITLE-C02-').update('')
                window['-OUTPUT-C02-'].update('')
            else:
                window['-OUTPUT-C02-'].update("Failed to create Artist!")

            updatelibtabs()

        ##########################
        if event == '-BUTTON-SEARCH-SONG-C04-':
            gui.createAlbumSongSearch = db.searchSong(values['-INPUT-SEARCH-SONG-C04-'])
            window['-TABLE-SEARCH-SONG-C04-'].update(values=  gui.createAlbumSongSearch)

        if event == '-ADD-SONG-C04-':
            #songName = values['-TABLE-SEARCH-SONG-C04-'][0]
            ## SOLUTION:
            try:
                songIndex = values['-TABLE-SEARCH-SONG-C04-'][0]
                print('song Index: ' + songIndex)
            except:
                print('select something')
                # break
            '''
            songTitle =  gui.createAlbumSongSearch[songIndex][0]
            songGenre =  gui.createAlbumSongSearch[songIndex][1]
            songReleaseYear =  gui.createAlbumSongSearch[songIndex][3]

            gui.songToLinkToAlbum.append([songTitle, songGenre, songReleaseYear])
            '''
            #db.insertSongWhileKnowingAlbumName( albumName, title, genre, releaseYear):

        # CREATE Album
        if event == '-BUTTON-C04-':
            albumTitle = values['-TITLE-C04-']

            print(gui.songToLinkToAlbum)

            if isValid(albumTitle):
                db.insertAlbum(0, albumTitle)
                window.FindElement('-TITLE-C04-').update('')

                gui.createAlbumSongSearch = []

        #####################

        # CREATE SONG
        if event == '-BUTTON-C05-':
            titleSong = values['-TITLE-C05-']
            genreSong = values['-GENRE-C05-'][0]
            #sourceLinksong = values['-SOURCE-C05-']
            releaseYearsong = values['-releaseYear-C05-']

            # print(genreSong)

            if isValid(titleSong, genreSong, releaseYearsong):
                db.insertSong(titleSong, genreSong, releaseYearsong)
                window.FindElement('-TITLE-C05-').update('')
                window.FindElement('-GENRE-C05-').update('')
                window.FindElement('-releaseYear-C05-').update('')
                window['-OUTPUT-C05-'].update('')
            else:
                window['-OUTPUT-C05-'].update("Failed to create Song!")

            # Force this window to have focus after window change (macos bug)
            window.TKroot.focus_force()
            updatelibtabs()

        ### LIBRARY EVENTS ###
        
        if event == '-BUTTON-L03-':

            albumIndex =  values['-TABLE-L03-'][0]
            albumToRating = gui.albumsTable[albumIndex][0]

            #db.changeWholeRating(albumToRating, values['-RATING-L03-'])
            updatelibtabs()

        # LIST SONGS - UPDATE RATING
        if event == '-BUTTON-L04-':

            ratingIndex = values['-TABLE-L04-'][0]
            if(ratingIndex != None):
                # if isValid(ratingIndex):
                # print(songsTable)
                songToRate = gui.songsTable[ratingIndex][0]
                db.changeWholeRating(songToRate, values['-RATING-L04-'])
                updatelibtabs()

        # DELETE SECTION

        if event == '-DELETE-BUTTON-L01-':

            try:
                recordIndex = values['-TABLE-L01-'][0]
                print(recordIndex)

                recordToDelete = gui.recordTable[recordIndex][0]
                recordDateToDelete = gui.recordTable[recordIndex][1]
                recordLocationToDelete = gui.recordTable[recordIndex][2]
                print(recordToDelete)
                db.deleteRecordLabel(recordToDelete, recordDateToDelete, recordLocationToDelete)
                updatelibtabs()
            except:
                print('select something')

        # DELETE ARTIST
        if event == '-DELETE-BUTTON-L02-':
            artistIndex = values['-TABLE-L02-'][0]

            artistToDelete = gui.artistTable[artistIndex][0]
            artistAge =  gui.artistTable[artistIndex][1]
            #artistInstrument =  gui.artistTable[artistIndex][3]
            #artistBand =  gui.artistTable[artistIndex][4]

            db.deleteArtist(artistToDelete)# , artistAge, artistInstrumentm, artistBand)
            updatelibtabs()

        # DELETE ALBUM
        if event == '-DELETE-BUTTON-L03-':
            albumIndex = values['-TABLE-L03-'][0]
            print(albumIndex)

            albumToDelete = gui.albumTable[albumIndex][0]
            print(albumToDelete)
            db.deleteSong(albumToDelete)
            updatelibtabs()

        # DELETE SONG
        if event == '-DELETE-BUTTON-L04-':
            songIndex = values['-TABLE-L04-'][0]
            print(songIndex)

            songToDelete = gui.songsTable[songIndex][0]
            print(songToDelete)
            db.deleteSong(songToDelete)
            updatelibtabs()

    # updatelibtabs()
    while True:

        event, values = window.read()

        # End progam when window is closed
        if event == sg.WINDOW_CLOSED:
            break

        # checkButtonPress(event, values)
        # SearchTab.searchEvents(event, window)

    # close the program
    window.close()


if __name__ == '__main__':
    main()
