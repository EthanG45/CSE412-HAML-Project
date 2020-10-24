# HAML_GUI

import PySimpleGUI as sg

sg.theme('dark grey 9')



# Define the window's contents

'''
searchTab = sg.Tab(
                        'search',

                        [[sg.Text("Search something")],
                        [sg.Input(key='-INPUT-SEARCH-')],
                        [sg.Button('search')]],
                        key='search_tab_1'
                    )#end of tab search
'''

#search song by name tab
searchSongTab = sg.Tab(
                        'searchSong',

                        [[sg.Text("Search Song")],
                        [sg.Input(key='-INPUT-SEARCH-SONG-')],
                        [sg.Button('search')]],
                        key='search_Song_tab'
                    )#end of tab search

#search artist name tab
searchArtistTab = sg.Tab(
                        'searchArtist',

                        [[sg.Text("Search artist")],
                        [sg.Input(key='-INPUT-SEARCH-ARTIST')],
                        [sg.Button('search')]],
                        key='search_Artist_tab'
                    )#end of tab search

# to be replaced by a nested tab group
deleteTab = sg.Tab(
                        'delete',

                        [[sg.Text("Delete something")],
                        [sg.Input(key='-INPUT-DElETE-')],
                        [sg.Button('delete')]],
                        key='delete_tab'

                    )#end of tab delete

# to be replaced by a nested tab group
createTab = sg.Tab(
                        'create',

                        [[sg.Text("Create something")],
                        [sg.Input(key='-INPUT-CREATE-')],
                        [sg.Button('create')]],
                        key = 'create_tab'
                    )#end of tab create

# the nested tab inside the Search tab
tabgroupSearch = sg.Tab( 
                'search',
                [[sg.TabGroup(
                [[
                    searchSongTab,

                    searchArtistTab
                  ]],  
                key = 'tabgroupSearch',
                enable_events = True
                )#end of TabGroup
            ]]
        )

# main layout this contains everything
layout = [[
            sg.TabGroup(
                [[
                    tabgroupSearch,

                    deleteTab,#to be replaced by a tab with tab groups
   
                    createTab #to be replaced by a tab with tab groups
   
                  
            ]],
                key = 'tabgroup',
                enable_events=True
            )#end of TabGroup
        ]
    ]#end of layout


# Create the window
window = sg.Window('H.A.M.L.', layout, font=("Roboto", 12), size = (400,300), finalize=True)

# start tab if we ont to start on a tab that is not at index 0 change select 0 to something
#window['tabgroup'].Widget.select(0)


# the place we will handle all updates to text using the key values.
while True:
    
    event, values = window.read()
    
    # End progam when window is closed
    if event == sg.WINDOW_CLOSED:
        break
    
    
    
    

# close the program
window.close()








