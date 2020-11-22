# HAML_GUI

import PySimpleGUI as sg
import sql
# import tabs/create
from tabs.create import CreateTab
from tabs.delete import DeleteTab
from tabs.update import UpdateTab
from tabs.library import LibraryTab
from tabs.search import SearchTab
from tabs.insights import InsightsTab
from tabs.feelingLucky import FeelingLuckyTab

db = sql.Database()  # import db
ct = CreateTab(db)
dt = DeleteTab(db)
ut = UpdateTab(db)
lt = LibraryTab(db)
st = SearchTab(db)
it = InsightsTab(db)
ft = FeelingLuckyTab(db)

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
                lt.libraryTabGUI(),
                it.insightsTabGUI(),
                ft.feelingLuckyTabGUI()
            ]],
            key='tabgroup',
            enable_events=True
        )  # end of TabGroup

    ]
    ]  # end of layout

    # Create the window
    window = sg.Window('H.A.M.L.', layout, font=(
        "Roboto", 12), size=(1920, 1080), finalize=True)

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

        if event == '-BUTTON-SEARCH-SONG-':
            temp = db.searchSong(values['-INPUT-SEARCH-SONG-'])
            window['-TABLE-SEARCH-SONG-'].update(values=temp)

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
            try:
                companyName = values['-companyName-C01-']
                labelLocation = values['-labelLocation-C01-']
                dateEstablished = values['-dateEstablished-C01-']
                titleName = values['-TITLE-C01-'][0]

                if isValid(companyName, dateEstablished, labelLocation, titleName):
                    db.insertRecordLabel(
                        titleName, companyName, dateEstablished, labelLocation)
                    #window['-TABLE-L01-'].update(values = db.getAllRecordLabels())
                    window.FindElement('-companyName-C01-').update('')
                    window.FindElement('-labelLocation-C01-').update('')
                    window.FindElement('-dateEstablished-C01-').update('')
                    window['-OUTPUT-C01-'].update("Record Label created")
                else:
                    window['-OUTPUT-C01-'].update(
                        "Failed to create Record Label!")
            except:
                sg.popup('Select an album please')

            # Force this window to have focus after window change (macos bug)
            window.TKroot.focus_force()
            updatelibtabs()

        # CREATE ARTIST
        if event == '-BUTTON-C02-':
            try:
                artistName = values['-ARTIST-C02-']
                artistAge = int(values['-AGE-C02-'])
                artistInstrument = values['-INSTRUMENT-C02-']
                artistBand = values['-BAND-C02-']
                titleName = values['-TITLE-C02-'][0]
                # recordLabelName = values['-RECORD-LABEL-NAME-C02-'][0]
                # recordLabelCity = values['-RECORD-LABEL-CITY-C02-'][1]

                '''recordLabelName, recordLabelCity'''

                if isValid(artistName, artistAge, artistInstrument, artistBand, titleName):
                    db.insertArtist(artistName, artistAge,
                                    artistInstrument, artistBand, titleName)
                    window.FindElement('-ARTIST-C02-').update('')
                    window.FindElement('-AGE-C02-').update('')
                    window.FindElement('-INSTRUMENT-C02-').update('')
                    window.FindElement('-BAND-C02-').update('')
                    window['-OUTPUT-C02-'].update("Artist created")
                else:
                    window['-OUTPUT-C02-'].update("Failed to create Artist!")
            except:
                sg.popup('Select an album please')

            updatelibtabs()

        ##########################

        # # CREATE ALBUM OG
        # if event == '-BUTTON-SEARCH-SONG-C04-':
        #     gui.createAlbumSongSearch = db.searchSong(values['-INPUT-SEARCH-SONG-C04-'])
        #     window['-TABLE-SEARCH-SONG-C04-'].update(values=  gui.createAlbumSongSearch)

        # if event == '-ADD-SONG-C04-':
        #     #songName = values['-TABLE-SEARCH-SONG-C04-'][0]
        #     ## SOLUTION:
        #     try:
        #         songIndex = values['-TABLE-SEARCH-SONG-C04-'][0]
        #         print('song Index: ' + songIndex)
        #     except:
        #         print('select something')
        #         # break
        #     '''
        #     songTitle =  gui.createAlbumSongSearch[songIndex][0]
        #     songGenre =  gui.createAlbumSongSearch[songIndex][1]
        #     songReleaseYear =  gui.createAlbumSongSearch[songIndex][3]

        #     gui.songToLinkToAlbum.append([songTitle, songGenre, songReleaseYear])
        #     '''
        #     #db.insertSongWhileKnowingAlbumName( albumName, title, genre, releaseYear):

        # CREATE Album
        if event == '-BUTTON-C04-':
            try:
                albumTitle = values['-ALBUM-TITLE-C04-']
                songTitle = values['-SONG-TITLE-C04-']
                songGenre = values['-GENRE-C04-'][0]
                songReleaseYear = values['-RELEASE-YEAR-C04-']
                artist = values['-ARTIST-TITLE-C04-'][0]

                if isValid(albumTitle, songTitle, songGenre, songReleaseYear, artist):
                    db.createSongAndAlbum(
                        artist, albumTitle, songTitle, songGenre, int(songReleaseYear))
                    window.FindElement('-ALBUM-TITLE-C04-').update('')
                    window.FindElement('-SONG-TITLE-C04-').update('')
                    window.FindElement('-RELEASE-YEAR-C04-').update('')
                    window['-OUTPUT-C04-'].update("Song and album created")
                else:
                    window['-OUTPUT-C04-'].update(
                        "Failed to create Album and Song!")
            except:
                window['-OUTPUT-C04-'].update('')
                sg.popup('Please select a genre and fill out other fields')

            # Force this window to have focus after window change (macos bug)
            window.TKroot.focus_force()
            updatelibtabs()

            # print(gui.songToLinkToAlbum)

            # if isValid(albumTitle):
            #     db.insertAlbum(0, albumTitle)
            #     window.FindElement('-TITLE-C04-').update('')

            #     gui.createAlbumSongSearch = []

        #####################

        # CREATE SONG
        if event == '-BUTTON-C05-':
            try:
                titleSong = values['-TITLE-C05-']
                genreSong = values['-GENRE-C05-'][0]
                #sourceLinksong = values['-SOURCE-C05-']
                releaseYearsong = values['-releaseYear-C05-']
                albumTitleName = values['-ALBUM-TITLE-C05-'][0]

                # print(genreSong)

                if isValid(titleSong, genreSong, releaseYearsong, albumTitleName):
                    db.insertSong(albumTitleName, titleSong,
                                  genreSong, releaseYearsong)
                    window.FindElement('-TITLE-C05-').update('')
                    window.FindElement('-releaseYear-C05-').update('')
                    window['-OUTPUT-C05-'].update("Song created")
                else:
                    window['-OUTPUT-C05-'].update("Failed to create Song!")
            except:
                sg.popup('Please select a genre, album and fill out other fields')

            # Force this window to have focus after window change (macos bug)
            window.TKroot.focus_force()
            updatelibtabs()

        ### LIBRARY EVENTS ###

        if event == '-BUTTON-L03-':
            albumIndex = values['-TABLE-L03-'][0]
            albumToRating = gui.albumsTable[albumIndex][0]

            #db.changeWholeRating(albumToRating, values['-RATING-L03-'])
            updatelibtabs()

        # LIST SONGS - UPDATE RATING
        if event == '-BUTTON-L04-':

            try:
                ratingIndex = values['-TABLE-L04-'][0]
                # if isValid(ratingIndex):
                # print(songsTable)
                songToRate = gui.songsTable[ratingIndex][0]
                db.changeWholeRating(songToRate, values['-RATING-L04-'])
                updatelibtabs()
            except:
                sg.popup('Please select a Song to rate')

        # DELETE SECTION

        if event == '-DELETE-BUTTON-L01-':

            try:
                recordIndex = values['-TABLE-L01-'][0]
                # print(recordIndex)
                recordToDelete = gui.recordTable[recordIndex][0]
                recordDateToDelete = gui.recordTable[recordIndex][2]
                recordLocationToDelete = gui.recordTable[recordIndex][3]
                # print(recordToDelete)
                db.deleteRecordLabel(
                    recordToDelete, recordDateToDelete, recordLocationToDelete)
            except:
                sg.popup('Please select a Record to delete')

            updatelibtabs()

        # DELETE ARTIST
        if event == '-DELETE-BUTTON-L02-':

            try:
                artistIndex = values['-TABLE-L02-'][0]

                artistToDelete = gui.artistTable[artistIndex][0]
                artistAge = gui.artistTable[artistIndex][1]
                #artistInstrument =  gui.artistTable[artistIndex][3]
                #artistBand =  gui.artistTable[artistIndex][4]

                # , artistAge, artistInstrumentm, artistBand)
                db.deleteArtist(artistToDelete, artistAge)
            except:
                sg.popup('Please select an Artist to delete')

            updatelibtabs()

        # DELETE ALBUM
        if event == '-DELETE-BUTTON-L03-':
            try:
                albumIndex = values['-TABLE-L03-'][0]
                print(albumIndex)
                albumToDelete = gui.albumsTable[albumIndex][0]
                albumDuration = gui.albumsTable[albumIndex][1]
                print(albumToDelete)
                # TODO: ADD albumDuration to this so shit
                # with the same name does noe fuck shit up
                db.deleteAlbum(albumToDelete)
            except:
                sg.popup('Please select an Album to delete')

            updatelibtabs()

        # DELETE SONG
        if event == '-DELETE-BUTTON-L04-':
            try:
                songIndex = values['-TABLE-L04-'][0]
                songToDelete = gui.songsTable[songIndex][0]
                print(songToDelete)
                db.deleteSong(songToDelete)
                updatelibtabs()
            except:
                sg.popup('Please select a song to delete')

        ### FEELING LUCKY EVENTS ###

        if event == '-BUTTON-ARTIST-F01-':
            temp = db.findArtistBySongName(values['-INPUT-ARTIST-F01-'])
            window['-TABLE-ARTIST-F01-'].update(values=temp)

        if event == '-BUTTON-SONG-F02-':
            try:
                year = values['-INPUT-YEAR-F02-']
                artist = values['-INPUT-ARTIST-F02-'][0]

                temp = db.findSongNameByYearAndArtist(artist, int(year))
                window['-TABLE-SONG-F02-'].update(values=temp)
            except:
                sg.popup('Please select a artist')

    # updatelibtabs()
    while True:

        event, values = window.read()

        # End progam when window is closed
        if event == sg.WINDOW_CLOSED:
            break

        checkButtonPress(event, values)
        # SearchTab.searchEvents(event, window)

    # close the program
    window.close()


if __name__ == '__main__':
    main()
