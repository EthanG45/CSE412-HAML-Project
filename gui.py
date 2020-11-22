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


def main():
    recordTable = db.getAllRecordLabels()
    artistTable = db.getAllArtists()
    albumsTable = db.getAllAlbums()
    songsTable = db.getAllSongs()

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
        recordTable = db.getAllRecordLabels()
        artistTable = db.getAllArtists()
        albumsTable = db.getAllAlbums()
        songsTable = db.getAllSongs()
        window['-TABLE-L01-'].update(values=recordTable)
        window['-TABLE-L02-'].update(values=artistTable)
        window['-TABLE-L04-'].update(values=albumsTable)
        window['-TABLE-L05-'].update(values=songsTable)

    def checkButtonPress(event, values):
        # events is formatted as follows
        # ('event', 'function', 'input', 'output', 'type')

        # window.Element('').focus=True
        # window.Element('').SetFocus()

        for elem in events:
            if event == elem[0]:
                # temp = elem[1](values[elem[2]])
                temp = elem[1](values[elem[2]])
                # temp = db.searchSong(values['-INPUT-SEARCH-SONG-'])
                window[elem[3]].update(values=temp)

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
                window['-OUTPUT-C01-'].update("Failed to create Record!")

            # Force this window to have focus after window change (macos bug)
            window.TKroot.focus_force()
            updatelibtabs()

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

        # Create Song
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

        if event == '-BUTTON-L05-':
            ratingIndex = values['-TABLE-L05-'][0]
            print(ratingIndex)
            # if isValid(ratingIndex):
            # print(songsTable)
            # songsTable[ratingIndex][4]
            # [
            #     ('AAlbert Song', 'Country', 977, 'stewart.com', 2014, Decimal('0')),
            #     ('American family', 'Metal', 240, 'dickerson-williams.com', 2008, Decimal('1.700000'))
            #     ]

    updatelibtabs()
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
