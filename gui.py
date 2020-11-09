# HAML_GUI

import PySimpleGUI as sg
# import sql as s1
from sql import searchSong

sg.theme('dark grey 9')
# Define the window's contents
# aString = "                                                             "#very important
aString = "                                                                       "

'''
searchTab = sg.Tab(
                        'search',

                        [[sg.Text("Search something")],
                        [sg.Input(key='-INPUT-SEARCH-')],
                        [sg.Button('search')]],
                        key='search_tab_1'
                    )#end of tab search
'''
### #### #### #### #### #### #### #### #### ###
#            CREATE TABLE TABS                #
### #### #### #### #### #### #### #### #### ###

createTableRecord = sg.Tab(
    'Record',

    [[sg.Text("Create A Table Record")],
     [sg.Text("Company Name")],
     [sg.Input(key='-companyName-')],
     [sg.Text("Date Established")],
     [sg.Input(key='-dateEstablished-')],
     [sg.Text("Label Location")],
     [sg.Input(key='-labelLocation-')],
     [sg.Text("Record Label Id")],
     [sg.Input(key='-recordLabelId-C01-')],
     [sg.Button('Create', key='-BUTTON-C01-')],
     [sg.Text(size=(10, 720), key='-OUTPUT-C01-')]],
    key='C01'
)  # end of tab Record

createTablePublishes = sg.Tab(
    'Publishes',

    [[sg.Text("Create A Publisher Delete this table maybe ... contains ID's only")],
     [sg.Text("album ID")],
     [sg.Input(key='-albumId-C02-')],
     [sg.Text("Record Label ID")],
     [sg.Input(key='-recordLabelId-C02-')],
     [sg.Button('Create', key='-BUTTON-C02-')],
     [sg.Text(size=(10, 720), key='-OUTPUT-C02-')]],
    key='C02'
)  # end of tab Publishes

createTableArtist = sg.Tab(
    'Artist',
    [[sg.Text("Create a Artist")],
     [sg.Text("Artist Name")],

     [sg.Text("Age")]],

    key='C03'
)

createTableMusician = sg.Tab(
    'Musician',
    [[sg.Text("Create a Musician")],
     [sg.Text("instrument")],

     [sg.Text("band")]

     ],
    key='C04'
)

createTablePlayed = sg.Tab(
    'Played',
    [[sg.Text("id's only so probable delete this tab")]],
    key='C05'
)

createTableAlbum = sg.Tab(
    'Album',
    [[sg.Text("---------")],
     [sg.Text("Album Duration")],

     [sg.Text("Title")],

     [sg.Text("Cover Art URL")]],

    key='C06'
)

createTableSong = sg.Tab(
    'Song',
    [[sg.Text("---------")],
     [sg.Text("Title")],

     [sg.Text("Genre")],

     [sg.Text("Song Duration")],

     [sg.Text("Source Link")],

     [sg.Text("Release Year")]

     ],
    key='C07'
)

createTableContains = sg.Tab(
    'Contains',
    [[sg.Text(" Contains has only Ids  ")]
     ],
    key='C08'
)
createTableMade = sg.Tab(
    'Made',
    [[sg.Text("---------")],
     [sg.Text("Known For?")]],
    key='C09'
)
createTableRating = sg.Tab(
    'Rating',
    [[sg.Text("---------")],
     [sg.Text("Num Of Rating")],

     [sg.Text("Average Rating")],

     [sg.Text("User Rating")]

     ],
    key='C10'
)

### #### #### #### #### #### #### #### #### ###
#          END OF CREATE TABLE TABS           #
### #### #### #### #### #### #### #### #### ###


### #### #### #### #### #### #### #### #### ###
#            DELETE TABLE TABS                #
### #### #### #### #### #### #### #### #### ###

deleteTableRecord = sg.Tab(
    'Record',

    [[sg.Text("Create A Table Record")],
     [sg.Text("Company Name")],
     [sg.Input(key='-companyName-D01-')],
     [sg.Text("Date Established")],
     [sg.Input(key='-dateEstablished-D01-')],
     [sg.Text("Label Location")],
     [sg.Input(key='-labelLocation-D01-')],
     [sg.Text("Record Label Id")],
     [sg.Input(key='-recordLabelId-D01-')],
     [sg.Button('Create', key='-BUTTON-D01-')],
     [sg.Text(size=(10, 720), key='-OUTPUT-D01-')]],
    key='D01'
)  # end of tab Record

deleteTablePublishes = sg.Tab(
    'Publishes',

    [[sg.Text("Create A Publisher Delete this table maybe ... contains ID's only")],
     [sg.Text("album ID ")],
     [sg.Input(key='-albumId-D02-')],
     [sg.Text("Record Label ID")],
     [sg.Input(key='-recordLabelId-D02-')],
     [sg.Button('Create', key='-BUTTON-D02-')],
     [sg.Text(size=(10, 720), key='-OUTPUT-D02-')]],
    key='D02'
)  # end of tab Publishes

deleteTableArtist = sg.Tab(
    'Artist',
    [[sg.Text("Create a Artist")],
     [sg.Text("Artist Name")],

     [sg.Text("Age")]],

    key='D03'
)

deleteTableMusician = sg.Tab(
    'Musician',
    [[sg.Text("Create a Musician")],
     [sg.Text("instrument")],
     [sg.Text("band")]

     ],
    key='D04'
)

deleteTablePlayed = sg.Tab(
    'Played',
    [[sg.Text("id's only so probable delete this tab")]],
    key='D05'
)

deleteTableAlbum = sg.Tab(
    'Album',
    [[sg.Text("---------")],
     [sg.Text("Album Duration")],

     [sg.Text("Title")],

     [sg.Text("Cover Art URL")]],

    key='D06'
)

deleteTableSong = sg.Tab(
    'Song',
    [[sg.Text("---------")],
     [sg.Text("Title")],

     [sg.Text("Genre")],

     [sg.Text("Song Duration")],

     [sg.Text("Source Link")],

     [sg.Text("Release Year")]

     ],
    key='D07'
)

deleteTableContains = sg.Tab(
    'Contains',
    [[sg.Text(" Contains has only Ids  ")]
     ],
    key='D08'
)
deleteTableMade = sg.Tab(
    'Made',
    [[sg.Text("---------")],
     [sg.Text("Known For?")]],
    key='D09'
)

deleteTableRating = sg.Tab(
    'Rating',
    [[sg.Text("---------")],
     [sg.Text("Num Of Rating")],

     [sg.Text("Average Rating")],

     [sg.Text("User Rating")]

     ],
    key='D10'
)

### #### #### #### #### #### #### #### #### ###
#          END OF DELETE TABLE TABS           #
### #### #### #### #### #### #### #### #### ###

# # search song by name tab
searchSongTab = sg.Tab(
    'Songs',

    [[sg.Text("Search Song", size=(1270, 1))],
     [sg.Input(key='-INPUT-SEARCH-SONG-')],
     [sg.Button('search', key='-BUTTON-SEARCH-SONG-')],
     [sg.Text( size=(10, 720), key='-OUTPUT-SEARCH-SONG-')]],
    key='search_Song_tab'
)  # end of tab search

# search artist name tab
searchArtistTab = sg.Tab(
    'Artists',

    [[sg.Text("Search artist")],
     [sg.Input(key='-INPUT-SEARCH-ARTIST-')],
     [sg.Button('search', key='-BUTTON-SEARCH-ARTIST-')],
     [sg.Text( size=(10, 40), key='-OUTPUT-SEARCH-ARTIST-')]],
    key='search_Artist_tab'
)  # end of tab search

# to be replaced by a nested tab group
deleteTab = sg.Tab(
    'Delete',

    [[sg.Text("Delete something")],
     [sg.Input(key='-INPUT-DElETE-')],
     [sg.Button('delete')]],
    key='delete_tab'
)  # end of tab delete

# to be replaced by a nested tab group
createTab = sg.Tab(
    'Create',
    [[sg.TabGroup(
        [[
            createTableRecord,
            createTablePublishes,  # ?
            createTableArtist,
            createTableMusician,
            createTablePlayed,
            createTableAlbum,
            createTableSong,
            createTableContains,  # ?
            createTableMade,
            createTableRating
        ]],
        key='tabgroupCreate',
        enable_events=True
    )  # end of TabGroup
    ]],

    key='create_tab'

)  # end of tab create

# the nested tab inside the Search tab
tabgroupSearch = sg.Tab(
    'Search',
    [[sg.TabGroup(
        [[
            searchSongTab,

            searchArtistTab
        ]],
        key='tabgroupSearch',
        enable_events=True
    )  # end of TabGroup
    ]]
)

# main layout this contains everything
layout = [[
    sg.TabGroup(
        [[
            tabgroupSearch,

            deleteTab,  # to be replaced by a tab with tab groups

            createTab  # to be replaced by a tab with tab groups

        ]],
        key='tabgroup',
        enable_events=True
    )  # end of TabGroup

]
]  # end of layout


# Create the window
window = sg.Window('H.A.M.L.', layout, font=(
    "Roboto", 12), size=(1280, 720), finalize=True)

# start tab if we ont to start on a tab that is not at index 0 change select 0 to something
# window['tabgroup'].Widget.select(0)


def checkButtonPress():

    if event == '-BUTTON-SEARCH-ARTIST-':
        temp = searchSong(values['-INPUT-SEARCH-ARTIST-'])
        window['-OUTPUT-SEARCH-ARTIST-'].update(temp)

        str1 = ""
        

        if values['-INPUT-SEARCH-ARTIST-'] == "001":
            window['-OUTPUT-SEARCH-ARTIST-'].update("clean")

    elif event == '-BUTTON-SEARCH-SONG-':
        temp = searchSong(values['-INPUT-SEARCH-SONG-'])
        
        str1 = ""

        if temp == "file not found":
            window['-OUTPUT-SEARCH-ARTIST-'].update(temp)
        else:
            for x in temp:
                str1 += x + " "

        window['-OUTPUT-SEARCH-SONG-'].update(str1)

        if values['-INPUT-SEARCH-SONG-'] == "001":
            window['-OUTPUT-SEARCH-SONG-'].update("clean")

        # window['-OUTPUT-SEARCH-SONG-'].update(values['-INPUT-SEARCH-SONG-'])


# the place we will handle all updates to text using the key values.
while True:

    event, values = window.read()

    # End progam when window is closed
    if event == sg.WINDOW_CLOSED:
        break

    checkButtonPress()


# def whichTab():
#    break


# close the program
window.close()


# print(searchSong("top that"))
print(searchSong("top that"))

"""def menu():
    options = ('Enter 1 to \n'
               'Enter 2 to \n'
               'Enter 3 to exit\n')
    choice = input(options)
    return int(choice)

print("Main Menu")

while True:
    choice = menu()
    if choice == 1:
        fn()
    elif choice == 2:
        fn1()
    elif choice == 3:
        break"""
