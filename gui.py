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
        return True;

    def checkButtonPress(event, values):
        print(event)
        # events is formatted as follows
        # ('event', 'function', 'input', 'output', 'type')
        for elem in events:
            if event == elem[0]:
                # temp = elem[1](values[elem[2]])
                temp = elem[1](values[elem[2]])
                # temp = db.searchSong(values['-INPUT-SEARCH-SONG-'])
                window[elem[3]].update(values = temp)

        if event == '-BUTTON-SEARCH-ARTIST-':
            temp = db.searchArtist(values['-INPUT-SEARCH-ARTIST-'])
            window['-TABLE-SEARCH-ARTIST-'].update(values = temp)

        if event == '-BUTTON-SEARCH-ALBUM-':
            temp = db.searchAlbum(values['-INPUT-SEARCH-ALBUM-'])
            window['-TABLE-SEARCH-ALBUM-'].update(values = temp)
        
        if event == '-BUTTON-SEARCH-MUSICIAN-':
            temp = db.searchMusician(values['-INPUT-SEARCH-MUSICIAN-'])
            window['-TABLE-SEARCH-MUSICIAN-'].update(values = temp)
        
        if event == '-BUTTON-SEARCH-RECORD-':
            temp = db.searchRecordLabel(values['-INPUT-SEARCH-RECORD-'])
            window['-TABLE-SEARCH-RECORD-'].update(values = temp)
       
        if event == '-BUTTON-C01-':
            companyName = values['-companyName-C01-']
            dateEstablished = values['-dateEstablished-C01-']
            labelLocation = values ['-labelLocation-C01-']
            if isValid(companyName, dateEstablished, labelLocation):
                db.insertRecordLabel(companyName, dateEstablished, labelLocation )
                #window['-TABLE-L01-'].update(values = db.getAllRecordLabels())
                window.FindElement('-companyName-C01-').update('')
                window.FindElement('-dateEstablished-C01-').update('')
                window.FindElement('-labelLocation-C01-').update('')

            else:
                 window['-OUTPUT-C01-'].update("Failed to create Record!")

        
        if event == '-BUTTON-C02-':
            artistName = values['-ARTIST-C02-']
            artistAge = values['-AGE-C02-']
            artistInstrument = values['-INSTRUMENT-C02-']
            artistBand = values['-BAND-C02-']

            if isValid(artistName, artistAge, artistInstrument, artistBand):
                db.insertArtist(artistName, artistAge, artistInstrument, artistBand )
                #window['-TABLE-L02-'].update(values = db.getAllArtists())

        '''
        if event == 'L01':
            window['-TABLE-L01-'].update(values = db.getAllRecordLabels())
        elif event == 'L02':
            window['-TABLE-L02-'].update(values = db.getAllArtists())
        elif event == 'L04':
            window['-TABLE-L04-'].update(values = db.getAllAlbums())
        elif event == 'L05':
            window['-TABLE-L05-'].update(values = db.getAllSongs())
        '''

        window['-TABLE-L01-'].update(values = db.getAllRecordLabels())
        window['-TABLE-L02-'].update(values = db.getAllArtists())
        window['-TABLE-L04-'].update(values = db.getAllAlbums())
        window['-TABLE-L05-'].update(values = db.getAllSongs())





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
