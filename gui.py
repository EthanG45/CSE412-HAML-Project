# HAML_GUI

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



# Define the window's contents


class GUI:
    def __init__(self):
        self.recordTable = db.getAllRecordLabels()
        self.artistTable = db.getAllArtists()
        self.albumsTable = db.getAllAlbums()
        self.songsTable = db.getAllSongs()
        # self.songToLinkToAlbum = []
        # self.createAlbumSongSearch = []
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

        self.updateWindow = None
        self.updateItem = ()


    def updateTables(self):
        self.recordTable = db.getAllRecordLabels()
        self.artistTable = db.getAllArtists()
        self.albumsTable = db.getAllAlbums()
        self.songsTable = db.getAllSongs()

# settingsTab = sg.Tab('setting', [[sg.theme_previewer()]], 'theme_tab')
def create_window():
        
    # main layout this contains everything
    layout = [[
        sg.TabGroup(
            [[
                lt.libraryTabGUI(),
                at.addTabGUI(),
                st.searchTabGUI(),
                # ut.updateTabGUI(),
                it.insightsTabGUI(),
                ft.feelingLuckyTabGUI(),
                sg.Tab('Theme', [[sg.Listbox(values = sg.theme_list(), key = '-THEME-LIST-', size = (20, 200), enable_events = True), sg.Button('SAVE NEW THEME', key = '-THEME-BUTTON-')]], key = '-THEME-TAB-'),
            ]],
            key='tabgroup',
            enable_events=True
        )  # end of TabGroup

    ]
    ]  # end of layout



    # Create the window
    # todo window size is still a little too big
    # todo app icon?
    window = sg.Window('H.A.M.L.', layout, font=(
        "Roboto", 12), size=(1920, 1080), finalize=True, element_justification='c', 
        icon = 'image/clyde.ico')
        

    return window

def main():
    sg.theme('Dark Grey 9')  # set window theme
    gui = GUI()
    
    window = create_window()
    
    #window = create_window()

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

        at.updateLists()
        window['-TITLE-C01-'].update(values=at.albumNameList)
        # window['-TITLE-C02-'].update(values=at.albumNameList)
        window['-INSTRUMENT-C02-'].update(values=at.instrumentList)
        window['-RECORD-TITLE-C02-'].update(values=at.recordLabelList)
        window['-ARTIST-TITLE-C04-'].update(values=at.artistNameList)
        window['-ALBUM-TITLE-C05-'].update(values=at.albumNameList)

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

    #def create_window():
    #   window = sg.Window('H.A.M.L.', layout, font=(
    #       "Roboto", 12), size=(1920, 1080), finalize=True)
    #
    #
    #
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

        if event == '-BUTTON-RATING-S01-':

            try:
                songIndex = values['-TABLE-SEARCH-SONG-'][0]
                newRating = values['-RATING-S01-']
                # songTitle = gui.searchSongTable[songIndex][0]
                songId = gui.searchSongTableId[songIndex][0]

                # db.changeWholeRating( songTitle, newRating)
                db.changeWholeRatingId(songId, newRating)

                tempSongName = gui.searchSongTable
                gui.searchSongTable = db.searchSong(gui.searchSongTable[songIndex][0])
                gui.searchSongTableId = db.searchSongId(tempSongName[songIndex][0])

                window['-TABLE-SEARCH-SONG-'].update(values=gui.searchSongTable)
                updatelibtabs()

            except:
                sg.popup('Please select a song')

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
                sg.popup('Please select a song')

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
                sg.popup('Please select a Artist')

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
                sg.popup('Please select a Album')

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
                sg.popup('Please select a Band')

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
                sg.popup('Please select a Record Label')

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
                    #window['-TABLE-L01-'].update(values = db.getAllRecordLabels())
                    window.FindElement('-companyName-C01-').update('')
                    window.FindElement('-labelLocation-C01-').update('')
                    window.FindElement('-dateEstablished-C01-').update('')
                    window['-OUTPUT-C01-'].update("Record Label added")
                else:
                    window['-OUTPUT-C01-'].update(
                        "Failed to add Record Label!")
            except:
                sg.popup('Select an album please')

            # Force this window to have focus after window change (macos bug)
            window.TKroot.focus_force()
            updatelibtabs()

        # ADD ARTIST
        if event == '-BUTTON-C02-':
            try:
                # TODO def createArtistAndSongAndAlbum(self, companyName, artistName, age, instrument, band, albumName, title, genre, releaseYear)
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
                sg.popup('Select instrument, genre, and record label please')

            updatelibtabs()

        ##########################

        # # ADD ALBUM OG
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

        # ADD SONG
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
                    window['-OUTPUT-C05-'].update("Song added")
                else:
                    window['-OUTPUT-C05-'].update("Failed to add Song!")
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
                print(temp)
                window['-TABLE-SONG-F02-'].update(values=temp)
            except:
                sg.popup('Please select a artist')

        if event == '-BUTTON-RECORD-LABEL-F03-':
            try:
                album = values['-INPUT-ALBUM-F03-'][0]

                name = db.findcompanyNameByAlbumName(album)[0][0]
                date = db.findRecLebDateByAlbumName(album)[0][0]
                location = db.findLocationByAlbumName(album)[0][0]
                # [('able seat', 'carry station team', 'Joshua Duran', 'EDM', 536, 'phillips-nelson.net', 2019, Decimal('2.500000'), 29419, 0)]
                temp = [(name, date, location)]
                window['-TABLE-RECORD-LABEL-F03-'].update(values=temp)
            except:
                sg.popup('Please select an album')

        if event == '-BUTTON-SONG-F04-':
            try:
                window['-TABLE-RECORD-LABEL-F04-'].update(values=db.findcompanyNameBySongName(values['-INPUT-SONG-F04-'][0]))
            except:
                sg.popup('Please select a song name')

        if event == '-BUTTON-RECORD-LABEL-F05-':
            try:
                window['-TABLE-RECORD-LABEL-F05-'].update(values=db.findcompanyNameByBandName(values['-INPUT-BAND-F05-'][0]))
            except:
                sg.popup('Please select a band name')

        if event == '-BUTTON-RECORD-LABEL-F06-':
            try:
                window['-TABLE-RECORD-LABEL-F06-'].update(values=db.findListOfCompanyNameByInstrument(values['-INPUT-INSTRUMENT-F06-'][0]))
            except:
                sg.popup('Please select an instrument')

        #### UPDATE EVENTS ####
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

                gui.updateWindow.close()

            except:
                sg.popup('Please select something to update')

        if event == '-UPDATE-BUTTON-L02-':
            try:
                gui.updateItem = gui.artistTable[values['-TABLE-L02-'][0]]
                gui.updateWindow = sg.Window('Update Artist', ut.updateArtistGUI(db.allAlbumName()), font=( "Roboto", 12), size=(1000, 700), finalize=True)

                button, updateValues = gui.updateWindow.read()
                if button == 'UPDATE':
                    artistName = updateValues['-ARTIST-U02-']
                    age = int(updateValues['-AGE-U02-'])
                    instrument = updateValues['-INSTRUMENT-U02-']
                    band = updateValues['-BAND-U02-']
                    albumName = updateValues['-TITLE-U02-'][0]

                    oldArtistName = gui.updateItem[0]

                    db.updateArtist(artistName, age, instrument, band, oldArtistName, albumName)
                    updatelibtabs()

                gui.updateWindow.close()
            except:
                sg.popup('Please select something to update')

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

                gui.updateWindow.close()

            except:
                sg.popup('Please select something to update')

        if event == '-UPDATE-BUTTON-L04-':
            try:
                gui.updateItem = gui.songsTable[values['-TABLE-L04-'][0]]
                gui.updateWindow = sg.Window('Update Song', ut.updateSongGUI(), font=(
                    "Roboto", 12), size=(1000, 500), finalize=True)

                button, updateValues = gui.updateWindow.read()
                if button == 'UPDATE':
                    title = updateValues['-TITLE-U04-']
                    genre = updateValues['-GENRE-U04-']
                    duration = int(updateValues['-DURATION-U04-'])
                    year = int(updateValues['-YEAR-U04-'])
                    oldTitle = gui.updateItem[0]

                    db.updateSong(title, genre, duration, year, oldTitle)
                    updatelibtabs()

                gui.updateWindow.close()
            except:
                sg.popup('Please select something to update')

    # updatelibtabs()

    while True:

        event, values = window.read()

        if window is None:
            window = create_window()
        
        ### THEME CHANGE ###

        if event == '-THEME-BUTTON-':
            try:
                print(values['-THEME-LIST-'][0])
                # ['DarkBlack']
                sg.theme(values['-THEME-LIST-'][0])
                window.close()
                window = create_window()
            except:
                sg.popup('Please select a theme')


        if event == sg.WINDOW_CLOSED:
            break

        checkButtonPress(event, values)

    # close the program
    window.close()


if __name__ == '__main__':
    main()
