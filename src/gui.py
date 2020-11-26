# HAML_GUI

# stuff for matlib plot
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.pyplot import figure
import PySimpleGUI as sg
import sql
from tabs.add import AddTab
from tabs.update import UpdateTab
from tabs.library import LibraryTab
from tabs.search import SearchTab
from tabs.insights import InsightsTab
from tabs.feelingLucky import FeelingLuckyTab

db = sql.Database()  # import db
at = AddTab(db)
ut = UpdateTab(db)
lt = LibraryTab(db)
st = SearchTab(db)
it = InsightsTab(db)
ft = FeelingLuckyTab(db)

events = []
st.addEvents(events)
mainWindowSize = (1470, 710)

# Define the window's contents

def popupGUI(message):
    layout = [[sg.Text(message)],
                [sg.Button('OK', bind_return_key=True)]]
    window = sg.Window('WARNING', layout, font=("Roboto", 12), size=(450, 75), finalize=True)
    return window

class GUI:
    def __init__(self):
        self.recordTable = db.getAllRecordLabels()
        self.artistTable = db.getAllArtists()
        self.albumsTable = db.getAllAlbums()
        self.songsTable = db.getAllSongs()
        self.searchSongTable = []
        self.searchSongTableId = []

        self.searchAlbumTable = []
        self.searchAlbumTableId = []

        self.searchArtistTable = []
        self.searchArtistTableId = []

        self.searchMusicianTable = []
        self.searchMusicianTableId = []

        self.searchRecordLabelTable = []
        self.searchRecordLabelTableId = []

        self.TabKeys = ['tabgroupSearch', 'tabgroup']
        self.textInputs = ['-INPUT-SEARCH-RECORD-', '-INPUT-SEARCH-BAND-','-INPUT-SEARCH-ALBUM-', '-INPUT-SEARCH-ARTIST-', '-INPUT-SEARCH-SONG-']
        self.allSearchTables = ['-TABLE-SEARCH-SONG-','-TABLE-SEARCH-ARTIST-','-TABLE-SEARCH-ALBUM-', '-TABLE-SEARCH-BAND-', '-TABLE-SEARCH-RECORD-', '-TABLE-SEARCH-SONG-']
        self.updateWindow = None
        self.updateItem = ()

    def updateTables(self):
        self.recordTable = db.getAllRecordLabels()
        self.artistTable = db.getAllArtists()
        self.albumsTable = db.getAllAlbums()
        self.songsTable = db.getAllSongs()


def create_window():
    plt.close('all')
    # main layout this contains everything
    layout = [[
        sg.TabGroup(
            [[
                lt.libraryTabGUI(),
                at.addTabGUI(),
                st.searchTabGUI(),
                it.insightsTabGUI(),
                ft.feelingLuckyTabGUI(),
                sg.Tab('Theme', [[sg.Listbox(values=sg.theme_list(), key='-THEME-LIST-', size=(20, 200), enable_events=True), sg.Button('SAVE NEW THEME', key='-THEME-BUTTON-')]], key='-THEME-TAB-'),
            ]],
            key='tabgroup',
            enable_events=True
        )  # end of TabGroup

    ]
    ]  # end of layout

    # Create the window
    window = sg.Window('H.A.M.L.', layout, font=(
        "Roboto", 12), size=mainWindowSize, finalize=True, element_justification='c')

    it.topTenSongsByUserPieFigure(window['-USR-SONG-CANVAS-IO1-G-'].TKCanvas, db)
    it.topTenSongsByAveragePieFigure(window['-AVG-SONG-CANVAS-IO1-G-'].TKCanvas, db)
    
    it.topTenAlbumsByUserPieFigure(window['-USR-ALBUM-CANVAS-IO2-G-'].TKCanvas, db)
    it.topTenAlbumsByAveragePieFigure(window['-AVG-ALBUM-CANVAS-IO2-G-'].TKCanvas, db)
    
    it.topTenSongsByUserWorstPieFigure(window['-USR-SONG-CANVAS-IO3-G-'].TKCanvas, db)
    it.topTenSongsByAverageWorstPieFigure(window['-AVG-SONG-CANVAS-IO3-G-'].TKCanvas, db)
    
    it.topTenAlbumsByUserWorstPieFigure(window['-USR-ALBUM-CANVAS-IO4-G-'].TKCanvas, db)
    it.topTenAlbumsByAverageWorstPieFigure(window['-AVG-ALBUM-CANVAS-IO4-G-'].TKCanvas, db)

    return window

def create_window_no_graph_update():
    plt.close('all')
    # main layout this contains everything
    layout = [[
        sg.TabGroup(
            [[
                lt.libraryTabGUI(),
                at.addTabGUI(),
                st.searchTabGUI(),
                it.insightsTabGUI(),
                ft.feelingLuckyTabGUI(),
                sg.Tab('Theme', [[sg.Listbox(values=sg.theme_list(), key='-THEME-LIST-', size=(20, 200), enable_events=True), sg.Button('SAVE NEW THEME', key='-THEME-BUTTON-')]], key='-THEME-TAB-'),
            ]],
            key='tabgroup',
            enable_events=True
        )  # end of TabGroup

    ]
    ]  # end of layout

    # Create the window
    window = sg.Window('H.A.M.L.', layout, font=(
        "Roboto", 12), size=mainWindowSize, finalize=True, element_justification='c',
        icon='image/HAML.png')
    
    return window


def main():
    plt.close('all')
    sg.theme('Dark Grey 9')  # set window theme
    gui = GUI()

    window = create_window()

    def isValid(*args):
        for elem in args:
            if elem == '':
                return False
        return True

    def updatelibtabs():
        plt.close('all')
        gui.updateTables()
        window['-TABLE-L01-'].update(values=gui.recordTable)
        window['-TABLE-L02-'].update(values=gui.artistTable)
        window['-TABLE-L03-'].update(values=gui.albumsTable)
        window['-TABLE-L04-'].update(values=gui.songsTable)

        at.updateLists()
        window['-TITLE-C01-'].update(values=at.albumNameList)
        window['-GENRE-C02-'].update(values=at.genreList)
        window['-INSTRUMENT-C02-'].update(values=at.instrumentList)
        window['-RECORD-TITLE-C02-'].update(values=at.recordLabelList)
        window['-GENRE-C04-'].update(values=at.genreList)
        window['-ARTIST-TITLE-C04-'].update(values=at.artistNameList)
        window['-ALBUM-TITLE-C05-'].update(values=at.albumNameList)
        window['-GENRE-C05-'].update(values=at.genreList)

        ft.updateLists()
        window['-INPUT-ARTIST-F02-'].update(values=ft.artistNameList)
        window['-INPUT-ALBUM-F03-'].update(values=ft.albumNameList)
        window['-INPUT-SONG-F04-'].update(values=ft.songNameList)
        window['-INPUT-BAND-F05-'].update(values=ft.bandNameList)
        window['-INPUT-INSTRUMENT-F06-'].update(values=ft.instrumentList)

        it.updateLists()
        window['-AVG-TABLE-I01-'].update(values=it.top10SongByAverage)
        window['-USER-TABLE-I01-'].update(values=it.top10SongByUser)
        window['-AVG-TABLE-I02-'].update(values=it.top10AlbumByAverage)
        window['-USER-TABLE-I02-'].update(values=it.top10AlbumByUser)
        window['-AVG-TABLE-I03-'].update(values=it.top10WorstSongByAverage)
        window['-USER-TABLE-I03-'].update(values=it.top10WorstSongByUser)
        window['-AVG-TABLE-I04-'].update(values=it.top10WorstAlbumByAverage)
        window['-USER-TABLE-I04-'].update(values=it.top10WorstAlbumByUser)
        
        '''it.topTenSongsByUserPieFigure(window['-USR-SONG-CANVAS-IO1-G-'].TKCanvas, db)
        it.topTenSongsByAveragePieFigure(window['-AVG-SONG-CANVAS-IO1-G-'].TKCanvas, db)
        
        it.topTenAlbumsByUserPieFigure(window['-USR-ALBUM-CANVAS-IO2-G-'].TKCanvas, db)
        it.topTenAlbumsByAveragePieFigure(window['-AVG-ALBUM-CANVAS-IO2-G-'].TKCanvas, db)
        
        it.topTenSongsByUserWorstPieFigure(window['-USR-SONG-CANVAS-IO3-G-'].TKCanvas, db)
        it.topTenSongsByAverageWorstPieFigure(window['-AVG-SONG-CANVAS-IO3-G-'].TKCanvas, db)
        
        it.topTenAlbumsByUserWorstPieFigure(window['-USR-ALBUM-CANVAS-IO4-G-'].TKCanvas, db)
        it.topTenAlbumsByAverageWorstPieFigure(window['-AVG-ALBUM-CANVAS-IO4-G-'].TKCanvas, db)'''

    def updateSearchTabs(inputValues):
        plt.close('all')
        gui.searchArtistTable = db.searchArtist(inputValues['-INPUT-SEARCH-ARTIST-'])
        gui.searchArtistTableId = db.searchArtistId(inputValues['-INPUT-SEARCH-ARTIST-'])
        window['-TABLE-SEARCH-ARTIST-'].update(values=gui.searchArtistTable)

        gui.searchSongTable = db.searchSong(inputValues['-INPUT-SEARCH-SONG-'])
        gui.searchSongTableId = db.searchSongId(inputValues['-INPUT-SEARCH-SONG-'])
        window['-TABLE-SEARCH-SONG-'].update(values=gui.searchSongTable)

        gui.searchAlbumTable = db.searchAlbum(inputValues['-INPUT-SEARCH-ALBUM-'])
        gui.searchAlbumTableId = db.searchAlbumId(inputValues['-INPUT-SEARCH-ALBUM-'])
        window['-TABLE-SEARCH-ALBUM-'].update(values=gui.searchAlbumTable)

        gui.searchMusicianTable = db.searchMusician(inputValues['-INPUT-SEARCH-BAND-'])
        gui.searchMusicianTableId = db.searchMusicianId(inputValues['-INPUT-SEARCH-BAND-'])
        window['-TABLE-SEARCH-BAND-'].update(values=gui.searchMusicianTable)

        gui.searchRecordLabelTable = db.searchRecordLabel(inputValues['-INPUT-SEARCH-RECORD-'])
        gui.searchRecordLabelTableId = db.searchRecordLabelId(inputValues['-INPUT-SEARCH-RECORD-'])
        window['-TABLE-SEARCH-RECORD-'].update(values=gui.searchRecordLabelTable)

    def checkButtonPress(event, values):
        
        ### SEARCH EVENTS ###
    
        if event == '-BUTTON-SEARCH-ARTIST-':
            gui.searchArtistTable = db.searchArtist(values['-INPUT-SEARCH-ARTIST-'])
            gui.searchArtistTableId = db.searchArtistId(values['-INPUT-SEARCH-ARTIST-'])
            window['-TABLE-SEARCH-ARTIST-'].update(values=gui.searchArtistTable)

        if event == '-BUTTON-SEARCH-SONG-':
            gui.searchSongTable = db.searchSong(values['-INPUT-SEARCH-SONG-'])
            gui.searchSongTableId = db.searchSongId(values['-INPUT-SEARCH-SONG-'])
            window['-TABLE-SEARCH-SONG-'].update(values=gui.searchSongTable)

        if event == '-BUTTON-SEARCH-ALBUM-':
            gui.searchAlbumTable = db.searchAlbum(values['-INPUT-SEARCH-ALBUM-'])
            gui.searchAlbumTableId = db.searchAlbumId(values['-INPUT-SEARCH-ALBUM-'])
            window['-TABLE-SEARCH-ALBUM-'].update(values=gui.searchAlbumTable)

        if event == '-BUTTON-SEARCH-BAND-':
            gui.searchMusicianTable = db.searchMusician(values['-INPUT-SEARCH-BAND-'])
            gui.searchMusicianTableId = db.searchMusicianId(values['-INPUT-SEARCH-BAND-'])
            window['-TABLE-SEARCH-BAND-'].update(values=gui.searchMusicianTable)

        if event == '-BUTTON-SEARCH-RECORD-':
            gui.searchRecordLabelTable = db.searchRecordLabel(values['-INPUT-SEARCH-RECORD-'])
            gui.searchRecordLabelTableId = db.searchRecordLabelId(values['-INPUT-SEARCH-RECORD-'])
            window['-TABLE-SEARCH-RECORD-'].update(values=gui.searchRecordLabelTable)

        ### DELETE SELECTED SEARCH ###

        if event == '-BUTTON-RATING-S01-':

            try:
                songIndex = values['-TABLE-SEARCH-SONG-'][0]
                newRating = values['-RATING-S01-']
                songId = gui.searchSongTableId[songIndex][0]

                db.changeWholeRatingId(songId, newRating)

                tempSongName = gui.searchSongTable
                gui.searchSongTable = db.searchSong(gui.searchSongTable[songIndex][0])
                gui.searchSongTableId = db.searchSongId(tempSongName[songIndex][0])

                window['-TABLE-SEARCH-SONG-'].update(values=gui.searchSongTable)
                updatelibtabs()

            except:
                popup = popupGUI('Please select a song')
                button, values = popup.read()
                popup.close()

        # delete searched song
        if event == '-DELETE-BUTTON-S01-':

            try:
                songIndex = values['-TABLE-SEARCH-SONG-'][0]
                songTitle = gui.searchSongTable[songIndex][0]

                db.deleteSongId(gui.searchSongTableId[songIndex][0])

                gui.searchSongTable = db.searchSong(songTitle)
                gui.searchSongTableId = db.searchSongId(songTitle)
                window['-TABLE-SEARCH-SONG-'].update(values=gui.searchSongTable)
                updatelibtabs()
            except:
                popup = popupGUI('Please select a song')
                button, values = popup.read()
                popup.close()

        # delete searched artist
        if event == '-DELETE-BUTTON-S02-':
            try:
                index = values['-TABLE-SEARCH-ARTIST-'][0]
                artistName = gui.searchArtistTable[index][0]
                artistID = gui.searchArtistTableId[index][0]

                db.deleteArtistId(artistID)

                gui.searchArtistTable = db.searchArtist(artistName)
                gui.searchArtistTableId = db.searchArtistId(artistName)
                window['-TABLE-SEARCH-ARTIST-'].update(values=gui.searchArtistTable)
                updatelibtabs()
            except:
                popup = popupGUI('Please select a Artist')
                button, values = popup.read()
                popup.close()

        # delete searched album
        if event == '-DELETE-BUTTON-S03-':
            try:
                index = values['-TABLE-SEARCH-ALBUM-'][0]
                albumName = gui.searchAlbumTable[index][0]
                albumID = gui.searchAlbumTableId[index][0]

                db.deleteAlbumByID(albumID)

                gui.searchAlbumTable = db.searchAlbum(albumName)
                gui.searchAlbumTableId = db.searchAlbumId(albumName)
                window['-TABLE-SEARCH-ALBUM-'].update(values=gui.searchAlbumTable)
                updatelibtabs()
            except:
                popup = popupGUI('Please select a Album')
                button, values = popup.read()
                popup.close()

        # delete searched musician
        if event == '-DELETE-BUTTON-S04-':
            try:
                index = values['-TABLE-SEARCH-BAND-'][0]
                artistName = gui.searchMusicianTable[index][0]
                bandName = gui.searchMusicianTable[index][3]
                artistID = gui.searchMusicianTableId[index][0]

                db.deleteArtistId(artistID)

                gui.searchMusicianTable = db.searchMusician(bandName)
                gui.searchMusicianTableId = db.searchMusicianId(bandName)
                window['-TABLE-SEARCH-BAND-'].update(values=gui.searchMusicianTable)
                updatelibtabs()
            except:
                popup = popupGUI('Please select a Band')
                button, values = popup.read()
                popup.close()

        # delete searched RecordLabel
        if event == '-DELETE-BUTTON-S05-':
            try:
                index = values['-TABLE-SEARCH-RECORD-'][0]
                someCompanyName = gui.searchRecordLabelTable[index][0]
                someRecordID = gui.searchRecordLabelTableId[index][0]

                db.deleteRecordLabelID(someRecordID)

                gui.searchRecordLabelTable = db.searchRecordLabel(someCompanyName)
                gui.searchRecordLabelTableId = db.searchRecordLabelId(someCompanyName)
                window['-TABLE-SEARCH-RECORD-'].update(values=gui.searchRecordLabelTable)
                updatelibtabs()
            except:
                popup = popupGUI('Please select a Record Label')
                button, values = popup.read()
                popup.close()

        ### ADD EVENTS ###

        # ADD RECORD LABEL
        if event == '-BUTTON-C01-':
            try:
                companyName = values['-companyName-C01-']
                labelLocation = values['-labelLocation-C01-']
                dateEstablished = values['-dateEstablished-C01-']
                titleName = values['-TITLE-C01-'][0]

                if isValid(companyName, dateEstablished, labelLocation, titleName):
                    db.insertRecordLabel(
                        titleName, companyName, dateEstablished, labelLocation)
                    window.FindElement('-companyName-C01-').update('')
                    window.FindElement('-labelLocation-C01-').update('')
                    window.FindElement('-dateEstablished-C01-').update('')
                    window['-OUTPUT-C01-'].update("Record Label added")
                else:
                    window['-OUTPUT-C01-'].update(
                        "Failed to add Record Label!")
            except:
                popup = popupGUI('Select an album please')
                button, values = popup.read()
                popup.close()

            # Force this window to have focus after window change (macos bug)
            window.TKroot.focus_force()
            updatelibtabs()

        # ADD ARTIST
        if event == '-BUTTON-C02-':
            try:
                artistName = values['-ARTIST-C02-']
                artistAge = int(values['-AGE-C02-'])
                artistInstrument = values['-INSTRUMENT-C02-'][0]
                artistBand = values['-BAND-C02-']
                albumTitle = values['-ALBUM-TITLE-C02-']
                songTitle = values['-SONG-TITLE-C02-']
                songGenre = values['-GENRE-C02-'][0]
                songReleaseYear = values['-RELEASE-YEAR-C02-']
                recordLabel = values['-RECORD-TITLE-C02-'][0]

                if isValid(artistName, artistAge, artistInstrument, artistBand, albumTitle, songTitle, songGenre, songReleaseYear, recordLabel):
                    db.createArtistAndSongAndAlbum(recordLabel, artistName, artistAge, artistInstrument, artistBand, albumTitle, songTitle, songGenre, int(songReleaseYear))
                    window.FindElement('-ARTIST-C02-').update('')
                    window.FindElement('-BAND-C02-').update('')
                    window.FindElement('-ALBUM-TITLE-C02-').update('')
                    window.FindElement('-SONG-TITLE-C02-').update('')
                    window['-OUTPUT-C02-'].update("Artist added")
                else:
                    window['-OUTPUT-C02-'].update("Failed to add Artist!")
            except:
                popup = popupGUI('Select instrument, genre, and record label please')
                button, values = popup.read()
                popup.close()

            updatelibtabs()

        # ADD Album
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
                    window['-OUTPUT-C04-'].update("Song and album added")
                else:
                    window['-OUTPUT-C04-'].update(
                        "Failed to add Album and Song!")
            except:
                window['-OUTPUT-C04-'].update('')
                popup = popupGUI('Please select a genre and fill out other fields')
                button, values = popup.read()
                popup.close()

            # Force this window to have focus after window change (macos bug)
            window.TKroot.focus_force()
            updatelibtabs()

        # ADD SONG
        if event == '-BUTTON-C05-':
            try:
                titleSong = values['-TITLE-C05-']
                genreSong = values['-GENRE-C05-'][0]
                releaseYearsong = values['-releaseYear-C05-']
                albumTitleName = values['-ALBUM-TITLE-C05-'][0]

                if isValid(titleSong, genreSong, releaseYearsong, albumTitleName):
                    db.insertSong(albumTitleName, titleSong,
                                  genreSong, releaseYearsong)
                    window.FindElement('-TITLE-C05-').update('')
                    window.FindElement('-releaseYear-C05-').update('')
                    window['-OUTPUT-C05-'].update("Song added")
                else:
                    window['-OUTPUT-C05-'].update("Failed to add Song!")
            except:
                popup = popupGUI('Please select a genre, album and fill out other fields')
                button, values = popup.read()
                popup.close()

            # Force this window to have focus after window change (macos bug)
            window.TKroot.focus_force()
            updatelibtabs()

        ### LIBRARY EVENTS ###

        if event == '-BUTTON-L03-':
            albumIndex = values['-TABLE-L03-'][0]
            albumToRating = gui.albumsTable[albumIndex][0]

            updatelibtabs()

        # LIST SONGS - UPDATE RATING
        if event == '-BUTTON-L04-':

            try:
                ratingIndex = values['-TABLE-L04-'][0]
                songToRate = gui.songsTable[ratingIndex][0]
                db.changeWholeRating(songToRate, values['-RATING-L04-'])
                updatelibtabs()
            except:
                popup = popupGUI('Please select a Song to rate')
                button, values = popup.read()
                popup.close()

        # DELETE SECTION

        # DELETE RECORD LABEL
        if event == '-DELETE-BUTTON-L01-':

            try:
                recordIndex = values['-TABLE-L01-'][0]
                recordToDelete = gui.recordTable[recordIndex][0]
                recordDateToDelete = gui.recordTable[recordIndex][2]
                recordLocationToDelete = gui.recordTable[recordIndex][3]
                db.deleteRecordLabel(
                    recordToDelete, recordDateToDelete, recordLocationToDelete)

                updateSearchTabs(values)
            except:
                popup = popupGUI('Please select a Record to delete')
                button, values = popup.read()
                popup.close()

            updatelibtabs()

        # DELETE ARTIST
        if event == '-DELETE-BUTTON-L02-':

            try:
                artistIndex = values['-TABLE-L02-'][0]

                artistToDelete = gui.artistTable[artistIndex][0]
                artistAge = gui.artistTable[artistIndex][1]
                db.deleteArtist(artistToDelete, artistAge)
                updateSearchTabs(values)
                
            except:
                popup = popupGUI('Please select an Artist to delete')
                button, values = popup.read()
                popup.close()

            updatelibtabs()

        # DELETE ALBUM
        if event == '-DELETE-BUTTON-L03-':
            try:
                albumIndex = values['-TABLE-L03-'][0]
                albumToDelete = gui.albumsTable[albumIndex][0]
                albumDuration = gui.albumsTable[albumIndex][1]
                db.deleteAlbum(albumToDelete)
                updateSearchTabs(values)
            except:
                popup = popupGUI('Please select an Album to delete')
                button, values = popup.read()
                popup.close()

            updatelibtabs()

        # DELETE SONG
        if event == '-DELETE-BUTTON-L04-':
            try:
                songIndex = values['-TABLE-L04-'][0]
                songToDelete = gui.songsTable[songIndex][0]
                db.deleteSong(songToDelete)
                updatelibtabs()
                updateSearchTabs(values)
            except:
                popup = popupGUI('Please select a song to delete')
                button, values = popup.read()
                popup.close()

        ### FEELING LUCKY EVENTS ###

        if event == '-BUTTON-ARTIST-F01-':
            temp = db.findArtistBySongName(values['-INPUT-ARTIST-F01-'])
            window['-TABLE-ARTIST-F01-'].update(values=temp)

        if event == '-BUTTON-SONG-F02-':
            try:
                year = int(values['-INPUT-YEAR-F02-'])
                artist = values['-INPUT-ARTIST-F02-'][0]

                temp = db.findSongNameByYearAndArtist(artist, int(year))
                window['-TABLE-SONG-F02-'].update(values=temp)
            except:
                popup = popupGUI('Please select an artist')
                button, values = popup.read()
                popup.close()

        if event == '-BUTTON-RECORD-LABEL-F03-':
            try:
                album = values['-INPUT-ALBUM-F03-'][0]

                name = db.findcompanyNameByAlbumName(album)[0][0]
                date = db.findRecLebDateByAlbumName(album)[0][0]
                location = db.findLocationByAlbumName(album)[0][0]
                temp = [(name, date, location)]
                window['-TABLE-RECORD-LABEL-F03-'].update(values=temp)
            except:
                popup = popupGUI('Please select an album')
                button, values = popup.read()
                popup.close()

        if event == '-BUTTON-SONG-F04-':
            try:
                window['-TABLE-RECORD-LABEL-F04-'].update(values=db.findcompanyNameBySongName(values['-INPUT-SONG-F04-'][0]))
            except:
                popup = popupGUI('Please select a song name')
                button, values = popup.read()
                popup.close()

        if event == '-BUTTON-RECORD-LABEL-F05-':
            try:
                window['-TABLE-RECORD-LABEL-F05-'].update(values=db.findcompanyNameByBandName(values['-INPUT-BAND-F05-'][0]))
            except:
                popup = popupGUI('Please select a band name')
                button, values = popup.read()
                popup.close()

        if event == '-BUTTON-RECORD-LABEL-F06-':
            try:
                window['-TABLE-RECORD-LABEL-F06-'].update(values=db.findListOfCompanyNameByInstrument(values['-INPUT-INSTRUMENT-F06-'][0]))
            except:
                popup = popupGUI('Please select an instrument')
                button, values = popup.read()
                popup.close()

        #### UPDATE EVENTS ####

        # UPDATE RECORD LABEL - LIBRARY TAB
        if event == '-UPDATE-BUTTON-L01-':
            try:
                gui.updateItem = gui.recordTable[values['-TABLE-L01-'][0]]

                gui.updateWindow = sg.Window('Update Record Label', ut.updateRecordLabelGUI(), font=("Roboto", 12), size=(1000, 500), finalize=True)

                button, updateValues = gui.updateWindow.read()
                if button == 'UPDATE':
                    companyName = updateValues['-COMPANY-NAME-U01-']
                    labelLocation = updateValues['-LABEL-LOCATION-U01-']
                    oldCompanyName = gui.updateItem[0]

                    db.updateRecordLabel(companyName, labelLocation, oldCompanyName)

                    updatelibtabs()
                    updateSearchTabs(values)

                gui.updateWindow.close()

            except:
                popup = popupGUI('Please select something to update')
                button, values = popup.read()
                popup.close()

        # UPDATE RECORD LABEL - SEARCH TAB
        if event == '-UPDATE-BUTTON-S05-':
            gui.updateItem = gui.recordTable[values['-TABLE-SEARCH-RECORD-'][0]]

            try:
                gui.updateWindow = sg.Window('Update Record Label', ut.updateRecordLabelGUI(), font=("Roboto", 12), size=(1000, 500), finalize=True)

                button, updateValues = gui.updateWindow.read()
                if button == 'UPDATE':
                    companyName = updateValues['-COMPANY-NAME-U01-']
                    labelLocation = updateValues['-LABEL-LOCATION-U01-']
                    oldCompanyName = gui.updateItem[0]

                    db.updateRecordLabel(companyName, labelLocation, oldCompanyName)

                    updatelibtabs()
                    updateSearchTabs(values)

                gui.updateWindow.close()

            except:
                popup = popupGUI('Please select something to update')
                button, values = popup.read()
                popup.close()

        # UPDATE ARTIST - LIBRARY TAB
        if event == '-UPDATE-BUTTON-L02-':
            try:
                gui.updateItem = gui.artistTable[values['-TABLE-L02-'][0]]
                gui.updateWindow = sg.Window('Update Artist', ut.updateArtistGUI(db.allInstName(), db.allAlbumName()), font=("Roboto", 12), size=(1000, 700), finalize=True)

                button, updateValues = gui.updateWindow.read()
                if button == 'UPDATE':
                    artistName = updateValues['-ARTIST-U02-']
                    age = int(updateValues['-AGE-U02-'])
                    instrument = updateValues['-INSTRUMENT-U02-'][0]
                    band = updateValues['-BAND-U02-']
                    albumName = updateValues['-TITLE-U02-'][0]

                    oldArtistName = gui.updateItem[0]

                    db.updateArtist(artistName, age, instrument, band, oldArtistName, albumName)
                    updatelibtabs()
                    updateSearchTabs(values)

                gui.updateWindow.close()
            except:
                popup = popupGUI('Please select something to update')
                button, values = popup.read()
                popup.close()

        # UPDATE ARTIST - SEARCH TAB
        if event == '-UPDATE-BUTTON-S02-':
            try:
                gui.updateItem = gui.artistTable[values['-TABLE-SEARCH-ARTIST-'][0]]
                gui.updateWindow = sg.Window('Update Artist', ut.updateArtistGUI(db.allInstName(), db.allAlbumName()), font=("Roboto", 12), size=(1000, 700), finalize=True)

                button, updateValues = gui.updateWindow.read()
                if button == 'UPDATE':
                    artistName = updateValues['-ARTIST-U02-']
                    age = int(updateValues['-AGE-U02-'])
                    instrument = updateValues['-INSTRUMENT-U02-'][0]
                    band = updateValues['-BAND-U02-']
                    albumName = updateValues['-TITLE-U02-'][0]

                    oldArtistName = gui.updateItem[0]

                    db.updateArtist(artistName, age, instrument, band, oldArtistName, albumName)
                    updatelibtabs()
                    updateSearchTabs(values)

                gui.updateWindow.close()
            except:
                popup = popupGUI('Please select something to update')
                button, values = popup.read()
                popup.close()

        # UPDATE ALBUM - LIBRARY TAB
        if event == '-UPDATE-BUTTON-L03-':
            try:
                gui.updateItem = gui.albumsTable[values['-TABLE-L03-'][0]]
                gui.updateWindow = sg.Window('Update Album', ut.updateAlbumGUI(), font=(
                    "Roboto", 12), size=(1000, 500), finalize=True, modal=True)

                button, updateValues = gui.updateWindow.read()
                if button == 'UPDATE':
                    title = updateValues['-TITLE-U03-']
                    duration = int(updateValues['-DURATION-U03-'])
                    oldTitle = gui.updateItem[0]

                    db.updateAlbum(title, duration, oldTitle)
                    updatelibtabs()
                    updateSearchTabs(values)

                gui.updateWindow.close()

            except:
                popup = popupGUI('Please select something to update')
                button, values = popup.read()
                popup.close()

        # UPDATE ALBUM - SEARCH TAB
        if event == '-UPDATE-BUTTON-S03-':
            try:
                gui.updateItem = gui.albumsTable[values['-TABLE-SEARCH-ALBUM-'][0]]
                gui.updateWindow = sg.Window('Update Album', ut.updateAlbumGUI(), font=(
                    "Roboto", 12), size=(1000, 500), finalize=True, modal=True)

                button, updateValues = gui.updateWindow.read()
                if button == 'UPDATE':
                    title = updateValues['-TITLE-U03-']
                    duration = int(updateValues['-DURATION-U03-'])
                    oldTitle = gui.updateItem[0]

                    db.updateAlbum(title, duration, oldTitle)
                    updatelibtabs()
                    updateSearchTabs(values)

                gui.updateWindow.close()

            except:
                popup = popupGUI('Please select something to update')
                button, values = popup.read()
                popup.close()

        # UPDATE SONG - LIBRARY TAB
        if event == '-UPDATE-BUTTON-L04-':
            try:
                gui.updateItem = gui.songsTable[values['-TABLE-L04-'][0]]
                gui.updateWindow = sg.Window('Update Song', ut.updateSongGUI(db.allGenre()), font=(
                    "Roboto", 12), size=(1000, 500), finalize=True)

                button, updateValues = gui.updateWindow.read()
                try:
                    if button == 'UPDATE':
                        title = updateValues['-TITLE-U04-']
                        genre = updateValues['-GENRE-U04-'][0]
                        duration = int(updateValues['-DURATION-U04-'])
                        year = int(updateValues['-YEAR-U04-'])
                        oldTitle = gui.updateItem[0]

                        db.updateSong(title, genre, duration, year, oldTitle)
                        updatelibtabs()
                        updateSearchTabs(values)

                    gui.updateWindow.close()
                except:
                    popup = popupGUI('Please fill out all the relevant fields')
                    button, values = popup.read()
                    popup.close()

            except:
                popup = popupGUI('Please select something to update')
                button, values = popup.read()
                popup.close()

        # UPDATE SONG - SEARCH TAB
        if event == '-UPDATE-BUTTON-S01-':
            try:
                gui.updateItem = gui.songsTable[values['-TABLE-SEARCH-SONG-'][0]]
                gui.updateWindow = sg.Window('Update Song', ut.updateSongGUI(db.allGenre()), font=(
                    "Roboto", 12), size=(1000, 500), finalize=True)

                button, updateValues = gui.updateWindow.read()
                try:
                    if button == 'UPDATE':
                        title = updateValues['-TITLE-U04-']
                        genre = updateValues['-GENRE-U04-'][0]
                        duration = int(updateValues['-DURATION-U04-'])
                        year = int(updateValues['-YEAR-U04-'])
                        oldTitle = gui.updateItem[0]

                        db.updateSong(title, genre, duration, year, oldTitle)
                        updatelibtabs()
                        updateSearchTabs(values)

                    gui.updateWindow.close()
                except:
                    popup = popupGUI('Please fill out all the relevant fields')
                    button, values = popup.read()
                    popup.close()

            except:
                popup = popupGUI('Please select something to update')
                button, values = popup.read()
                popup.close()

    while True:

        event, values = window.read()

        if window is None:
            window = create_window()

        ### THEME CHANGE ###

        if event == '-THEME-BUTTON-':
            try:
                sg.theme(values['-THEME-LIST-'][0])
                plt.close('all')
                window.close()
                window = create_window()
            except:
                popup = popupGUI('Please select a theme')
                button, values = popup.read()
                popup.close()

        if event == sg.WINDOW_CLOSED:
            break

        checkButtonPress(event, values)

    # close the program
    window.close()
    db.closeConnection()

if __name__ == '__main__':
    main()
