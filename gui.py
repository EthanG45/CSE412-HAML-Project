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

sg.theme('Dark Purple 3')  # set window theme

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

    def checkButtonPress(event, values):
        
        # events is formatted as follows
        # ('event', 'function', 'input', 'output', 'type')
        for elem in events:
            if event == elem[0]:
                # temp = elem[1](values[elem[2]])
                temp = elem[1](values[elem[2]])
                # temp = db.searchSong(values['-INPUT-SEARCH-SONG-'])
                window[elem[3]].update(values = temp)
        # dt.check
        # ut.check



        '''if event == '-BUTTON-SEARCH-ARTIST-':
            temp = db.searchArtist(values['-INPUT-SEARCH-ARTIST-'])
            window['-OUTPUT-SEARCH-ARTIST-'].update(temp)

            str1 = ""

        elif event == '-BUTTON-SEARCH-SONG-':
            temp = db.searchSong(values['-INPUT-SEARCH-SONG-'])
            window['-TABLE-SEARCH-SONG-'].update(temp)
        '''
        # elif event == tuple.el1:
        #     temp = tuple.el2(values[tuple.el3])
        #     window[tuple.el4].update(temp)

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