# HAML_GUI

import PySimpleGUI as sg
# import sql as s1
import sql


db = sql.Database()

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

    [[sg.Text("Create A Table Record", size=(1270, 1))],
     [sg.Text("Company Name")],
     [sg.Input(key='-companyName-C01-')],
     [sg.Text("Date Established")],
     [sg.Input(key='-dateEstablished-C01-')],
     [sg.Text("Label Location")],
     [sg.Input(key='-labelLocation-C01-')],
     [sg.Text("Record Label Id")],
     [sg.Input(key='-recordLabelId-C01-')],
     [sg.Button('CREATE', key='-BUTTON-C01-')],
     [sg.Text(size=(100, 720), key='-OUTPUT-C01-')]],
    key='C01'
)  # end of tab Record

'''
createTablePublishes = sg.Tab(
    'Publishes',

    [[sg.Text("Create A Publisher Delete this table maybe ... contains ID's only")],
     [sg.Text("album ID")],
     [sg.Input(key='-albumId-C02-')],
     [sg.Text("Record Label ID")],
     [sg.Input(key='-recordLabelId-C02-')],
     [sg.Button('CREATE', key='-BUTTON-C02-')],
     [sg.Text(size=(100, 720), key='-OUTPUT-C02-')]],
    key='C02'
)  # end of tab Publishes
'''

createTableArtist = sg.Tab(
    'Artist',

    [[sg.Text("Create a Artist")],
     [sg.Text("Artist Name")],
     [sg.Input(key='-ARTIST-C02-')],
     [sg.Text("Age")],
     [sg.Input(key='-AGE-C02-')],

    #Musician elements
     [sg.Text("Instrument")],
     [sg.Input(key='-INSTRUMENT-C02-')],
     [sg.Text("band")],
     [sg.Input(key='-BAND-C02-')],

     [sg.Button('CREATE', key='-BUTTON-C02-')],
     [sg.Text(size=(100, 720), key='-OUTPUT-C02-')]],
    key='C02'
)

'''
createTableMusician = sg.Tab(
    'Musician',
    [[sg.Text("Create a Musician")],
     [sg.Text("Select already existing unique artist by name")],
     [sg.Input(key='-ARTIST-C03-')],
     [sg.Text("Instrument")],
     [sg.Input(key='-INSTRUMENT-C03-')],
     [sg.Text("band")],
     [sg.Input(key='-BAND-C03-')],

     [sg.Button('CREATE', key='-BUTTON-C03-')],
     [sg.Text(size=(100, 720), key='-OUTPUT-C03-')]
     ],

    key='C03'
)'''

'''
createTablePlayed = sg.Tab(
    'Played',
    [[sg.Text("id's only so probable delete this tab")],
    [sg.Button('CREATE', key='-BUTTON-C05-')],
    [sg.Text(size=(100, 720), key='-OUTPUT-C05-')]
    ],
    key='C05'
)
'''

createTableAlbum = sg.Tab(
    'Album',
    [[sg.Text("Create a Album")],
     [sg.Text("Album Duration")],
     [sg.Input(key='-ALBUM-DURATION-C04-')],
     [sg.Text("Title")],
     [sg.Input(key='-TITLE-C04-')],
     [sg.Text("Cover Art URL")],
     [sg.Input(key='-URL-C04-')],
     [sg.Button('CREATE', key='-BUTTON-C04-')],
     [sg.Text(size=(100, 720), key='-OUTPUT-C04-')]
     ],

    key='C04'
)
daySize = 5
monthSize = 7
yearSize = 10

createTableSong = sg.Tab(
    'Song',
    [[sg.Text("Create a song")],
     [sg.Text("Title")],
     [sg.Input(key='-TITLE-C05-')],
     [sg.Text("Genre")],
     [sg.Input(key='-GENRE-C05-')],
     [sg.Text("Song Duration")],
     [sg.Input(key='-SONG-DURATION-C05-')],
     [sg.Text("Source Link")],
     [sg.Input(key='-SOURCE-C05-')],
     [sg.Text("Release Year")],
     [sg.Text("Day",size=(daySize, 1)), sg.Text("Month",size=(monthSize, 1)), sg.Text("Year",size=(yearSize, 1))],
     [sg.Input(key='-DAY-C05-', size=(daySize, 1)),     sg.Input(key='-MONTH-C05-', size=(monthSize, 1)),     sg.Input(key='-YEAR-C05-', size=(yearSize, 1))],

     #[sg.Input(key='-RELEASE-YEAR-C07-')],
     #[sg.Button('CREATE', key='-BUTTON-C07-')],

     [sg.Text(size=(100, 720), key='-OUTPUT-C05-')]

     ],
    key='C05'
)

'''
createTableContains = sg.Tab(
    'Contains',
    [[sg.Text(" Contains has only Ids  ")],
    [sg.Input(key='-d-C08-')],
    [sg.Button('CREATE', key='-BUTTON-C08-')],
    [sg.Text(size=(100, 720), key='-OUTPUT-C08-')]
    ],
    key='C08'
)'''

createTableMade = sg.Tab(
    'Made',
    [[sg.Text("---------")],
     [sg.Text("Known For?")],
     [sg.Input(key='-KNOWN-FOR-C06-')],

     [sg.Button('CREATE', key='-BUTTON-C06-')],
     [sg.Text(size=(100, 720), key='-OUTPUT-C06-')]
     ],
    key='C06'
)

createTableRating = sg.Tab(
    'Rating',
    [[sg.Text("create a rating")],
     [sg.Text("Number Of Rating")],
     [sg.Input(key='-NUM-OF-RATING-C07-')],
     [sg.Text("Average Rating")],
     [sg.Input(key='-AVERAGE-RATING-C07-')],
     [sg.Text("User Rating")],
     [sg.Input(key='-USER-RATING-C07-')],

     [sg.Button('CREATE', key='-BUTTON-C07-')],
     [sg.Text(size=(100, 720), key='-OUTPUT-C07-')]
     ],
    key='C07'
)

### #### #### #### #### #### #### #### #### ###
#          END OF CREATE TABLE TABS           #
### #### #### #### #### #### #### #### #### ###


### #### #### #### #### #### #### #### #### ###
#            DELETE TABLE TABS                #
### #### #### #### #### #### #### #### #### ###

deleteTableRecord = sg.Tab(
    'Record',

    [[sg.Text("Create A Table Record", size=(1270, 1))],
     [sg.Text("Company Name")],
     [sg.Input(key='-companyName-D01-')],
     [sg.Text("Date Established")],
     [sg.Input(key='-dateEstablished-D01-')],
     [sg.Text("Label Location")],
     [sg.Input(key='-labelLocation-D01-')],
     [sg.Text("Record Label Id")],
     [sg.Input(key='-recordLabelId-D01-')],
     [sg.Button('DELETE', key='-BUTTON-D01-')],
     [sg.Text(size=(100, 700), key='-OUTPUT-D01-')]],
    key='D01'
)  # end of tab Record

'''
deleteTablePublishes = sg.Tab(
    'Publishes',

    [[sg.Text("Create A Publisher Delete this table maybe ... contains ID's only")],
     [sg.Text("album ID ")],
     [sg.Input(key='-albumId-D02-')],
     [sg.Text("Record Label ID")],
     [sg.Input(key='-recordLabelId-D02-')],
     [sg.Button('DELETE', key='-BUTTON-D02-')],
     [sg.Text(size=(100, 700), key='-OUTPUT-D02-')]],
    key='D02'
)  # end of tab Publishes
'''

deleteTableArtist = sg.Tab(
    'Artist',
    [[sg.Text("Create a Artist")],
     [sg.Text("Artist Name")],
     [sg.Input(key='-ARTIST-NAME-D02-')],
     [sg.Text("Age")],
     [sg.Input(key='-AGE-D02-')],

    #Musician elements
     [sg.Text("Instrument")],
     [sg.Input(key='-INSTRUMENT-D02-')],
     [sg.Text("band")],
     [sg.Input(key='-BAND-D02-')],

     [sg.Button('DELETE', key='-BUTTON-D02-')],
     [sg.Text(size=(100, 700), key='-OUTPUT-D02-')]],

    key='D02'
)

'''
deleteTableMusician = sg.Tab(
    'Musician',
    [[sg.Text("Create a Musician")],
     [sg.Text("Instrument")],
     [sg.Input(key='-INSTRUMENT-D03-')],
     [sg.Text("band")],
     [sg.Input(key='-BAND-D03-')],
     [sg.Button('DELETE', key='-BUTTON-D03-')],
     [sg.Text(size=(100, 700), key='-OUTPUT-D03-')]
     ],
    key='D03'
)'''

#deleteTablePlayed = sg.Tab(
#    'Played',
#    [[sg.Text("!!!!!!!id's only so probable delete this tab")]
#     [sg.Button('DELETE', key='-BUTTON-D05-')],
#     [sg.Text(size=(100, 700), key='-OUTPUT-D05-')]
#    ],
#    key='D05'
#)

deleteTableAlbum = sg.Tab(
    'Album',
    [[sg.Text("---------")],
     [sg.Text("Album Duration")],
     [sg.Input(key='-ALBUM-DURATION-D04-')],

     [sg.Text("Title")],
     [sg.Input(key='-TITLE-D04-')],

     [sg.Text("Cover Art URL")],
     [sg.Input(key='-COVER ART URL-D04-')],

     [sg.Button('DELETE', key='-BUTTON-D04-')],
     [sg.Text(size=(100, 700), key='-OUTPUT-D04-')]
     
     ],

    key='D04'
)

deleteTableSong = sg.Tab(
    'Song',
    [[sg.Text("---------")],
     [sg.Text("Title")],
     [sg.Input(key='-TITLE-D05-')],

     [sg.Text("Genre")],
     [sg.Input(key='-GENRE-D05-')],

     [sg.Text("Song Duration")],
     [sg.Input(key='-SONG-DURATION-D05-')],

     [sg.Text("Source Link")],
     [sg.Input(key='-SOURCE-LINK-D05-')],

     [sg.Text("Release date")],
     [sg.Text("Day",size=(daySize, 1)), sg.Text("Month",size=(monthSize, 1)), sg.Text("Year",size=(yearSize, 1))],
     [sg.Input(key='-DAY-D05-', size=(daySize, 1)), sg.Input(key='-MONTH-D05-', size=(monthSize, 1)), sg.Input(key='-YEAR-D05-', size=(yearSize, 1))],

     [sg.Button('DELETE', key='-BUTTON-D05-')],
     [sg.Text(size=(100, 700), key='-OUTPUT-D05-')]

     ],
    key='D05'
)
'''
deleteTableContains = sg.Tab(
    'Contains',
    [[sg.Text(" Contains has only Ids  ")]
     ],
    key='D06'
)
'''
deleteTableMade = sg.Tab(
    'Made',
    [[sg.Text("---------")],

     [sg.Text("Known For?")],

     [sg.Button('DELETE', key='-BUTTON-D06-')],
     [sg.Text(size=(100, 700), key='-OUTPUT-D06-')]
     ],
    key='D06'
)

deleteTableRating = sg.Tab(
    'Rating',
    [[sg.Text("---------")],
     [sg.Text("Num Of Rating")],

     [sg.Text("Average Rating")],

     [sg.Text("User Rating")],

     [sg.Button('DELETE', key='-BUTTON-D07-')],
     [sg.Text(size=(100, 700), key='-OUTPUT-D07-')]

     ],
    key='D07'
)

### #### #### #### #### #### #### #### #### ###
#          END OF DELETE TABLE TABS           #
### #### #### #### #### #### #### #### #### ###


### #### #### #### #### #### #### #### #### ###
#           START UPDATE TABLE TABS           #
### #### #### #### #### #### #### #### #### ###

updateTableRecord = sg.Tab(
    'Record',

    [[sg.Text("Update A Table Record", size=(1270, 1))],
     [sg.Text("Company Name")],
     [sg.Input(key='-companyName-U01-')],
     [sg.Text("Date Established")],
     [sg.Input(key='-dateEstablished-U01-')],
     [sg.Text("Label Location")],
     [sg.Input(key='-labelLocation-U01-')],
     [sg.Text("Record Label Id")],
     [sg.Input(key='-recordLabelId-U01-')],
     [sg.Button('DELETE', key='-BUTTON-U01-')],
     [sg.Text(size=(100, 700), key='-OUTPUT-U01-')]],
    key='U01'
)  # end of tab Record

updateTableArtist = sg.Tab(
    'Artist',
    [[sg.Text("Create a Artist")],
     [sg.Text("Artist Name")],
     [sg.Input(key='-ARTIST-NAME-U02-')],
     [sg.Text("Age")],
     [sg.Input(key='-AGE-U02-')],

    #Musician elements
     [sg.Text("Instrument")],
     [sg.Input(key='-INSTRUMENT-U02-')],
     [sg.Text("band")],
     [sg.Input(key='-BAND-U02-')],

     [sg.Button('DELETE', key='-BUTTON-U02-')],
     [sg.Text(size=(100, 700), key='-OUTPUT-U02-')]],

    key='U02'
)

'''
updateTableMusician = sg.Tab(
    'Musician',
    [[sg.Text("Create a Musician !!!! delete")],
     [sg.Text("Instrument")],
     [sg.Input(key='-INSTRUMENT-U03-')],
     [sg.Text("band")],
     [sg.Input(key='-BAND-U03-')],
     [sg.Button('DELETE', key='-BUTTON-U03-')],
     [sg.Text(size=(100, 700), key='-OUTPUT-U03-')]
     ],
    key='U03'
)
'''

updateTableAlbum = sg.Tab(
    'Album',
    [[sg.Text("---------")],
     [sg.Text("Album Duration")],
     [sg.Input(key='-ALBUM-DURATION-U04-')],

     [sg.Text("Title")],
     [sg.Input(key='-TITLE-U04-')],

     [sg.Text("Cover Art URL")],
     [sg.Input(key='-COVER ART URL-U04-')],

     [sg.Button('DELETE', key='-BUTTON-U04-')],
     [sg.Text(size=(100, 700), key='-OUTPUT-U04-')]
     
     ],

    key='U04'
)

updateTableSong = sg.Tab(
    'Song',
    [[sg.Text("---------")],
     [sg.Text("Title")],
     [sg.Input(key='-TITLE-U05-')],

     [sg.Text("Genre")],
     [sg.Input(key='-GENRE-U05-')],

     [sg.Text("Song Duration")],
     [sg.Input(key='-SONG-DURATION-U05-')],

     [sg.Text("Source Link")],
     [sg.Input(key='-SOURCE-LINK-U05-')],

     [sg.Text("Release date")],
     
     [sg.Text("Day",size=(daySize, 1)), sg.Text("Month",size=(monthSize, 1)), sg.Text("Year",size=(yearSize, 1))],
     [sg.Input(key='-DAY-U05-', size=(daySize, 1)), sg.Input(key='-MONTH-U05-', size=(monthSize, 1)), sg.Input(key='-YEAR-U05-', size=(yearSize, 1))],

     [sg.Button('DELETE', key='-BUTTON-U05-')],
     [sg.Text(size=(100, 700), key='-OUTPUT-U05-')]

     ],
    key='U05'
)

updateTableMade = sg.Tab(
    'Made',
    [[sg.Text("---------")],

     [sg.Text("Known For?")],

     [sg.Button('DELETE', key='-BUTTON-U06-')],
     [sg.Text(size=(100, 700), key='-OUTPUT-U06-')]
     ],
    key='U06'
)

updateTableRating = sg.Tab(
    'Rating',
    [[sg.Text("---------")],
     [sg.Text("Num Of Rating")],

     [sg.Text("Average Rating")],

     [sg.Text("User Rating")],

     [sg.Button('DELETE', key='-BUTTON-U07-')],
     [sg.Text(size=(100, 700), key='-OUTPUT-U07-')]

     ],
    key='U0i'
)

### #### #### #### #### #### #### #### #### ###
#           END OF UPDATE TABLE TABS          #
### #### #### #### #### #### #### #### #### ###

### #### #### #### #### #### #### #### #### ###
#               START OF LIB TABS             #
### #### #### #### #### #### #### #### #### ###

libSize  = (1270, 700)

testlistbox = ['1' , '2' , '3', '4', '5' , "just testing this", 'what is this', '6', '7', '8', '9', '10']

libTableRecord = sg.Tab(
    'Record',

    [[sg.Text("Records")],
        [sg.Listbox(testlistbox, key = '-RECORD-L01-', size=(1270, 1))]
        ],
    key='L01'
)  # end of tab Record

libTableArtist = sg.Tab(
    'Artist',
    [[sg.Text("Artists")],
        [sg.Listbox(testlistbox, key = '-ARTIST-L02-', size = libSize)]
    ],
    key='L02'
)

libTableAlbum = sg.Tab(
    'Album',
    [[sg.Text("Albums")],
        [sg.Listbox(testlistbox, key = '-ALBUM-L04-', size = libSize)]
     ],

    key='L04'
)

songlisttable = [['title', 'songId', 'genre{}', 'year','songDuration','sourceLink'],['1', '2', '3', '5','6'],['q', 'w', 'e', 'r','t'] ]
songList2 = db.getAllSongs()

libTableSong = sg.Tab(
    'Song',
    [[sg.Text("Songs")],
     [sg.Listbox(values = testlistbox, key = '-SONG-L05-', size = libSize, enable_events=True)]
        ##[sg.Table(values = songlisttable, headings= [' Title ', ' songID ', ' genre ', ' year ', ' Duration ', 'sourceLink'],key = '-SONG-L05-', enable_events=True)]
     ],

    key='L05'
)

libTableMade = sg.Tab(
    'Made', 
    [[sg.Text("Made")],
        [sg.Listbox(testlistbox, key = '-MADE-L06-', size = libSize)]
     ],
    key='L06'
)

libTableRating = sg.Tab(
    'Rating',
    [[sg.Text("Ratings")],
        [sg.Listbox(testlistbox, key = '-RATING-L07-', size = libSize)]
     ],
    key='L07'
) 

def libtabUpdater():
    if event == '-L01-':
        print('-RECORD-L01-')

    elif event == 'L02-':
        print('-ARTIST-L02-')

    elif event == '-L04-':
        #window['-SONG-L02-'].update(songList)
        print('-ALBUM-L04-')

    elif event == '-L05-':
        #songList = update list using some sql converted into a list
        songList = db.getAllSongs()
        window['-SONG-L05-'].update(songList)

        print('-SONG-L05-')

    elif event == '-L06-':
        #window['-SONG-L02-'].update(songList)

        print('-MADE-L06-')

    elif event == '-L07-':
        #window['-SONG-L02-'].update(songList)

        print('-RATING-L07-')



### #### #### #### #### #### #### #### #### ###
#                END OF LIB TABS              #
### #### #### #### #### #### #### #### #### ###

# # search song by name tab
searchSongTab = sg.Tab(
    'Songs',

    [[sg.Text("Search Song", size=(1270, 1))],
     [sg.Input(key='-INPUT-SEARCH-SONG-')],
     [sg.Button('search', key='-BUTTON-SEARCH-SONG-')],
     [sg.Text(size=(100, 720), key='-OUTPUT-SEARCH-SONG-')]],
    key='search_Song_tab'
)  # end of tab search


libraryTab = sg.Tab(
    'Library',
      
    [
        [sg.Button('Restart Song', button_color=(sg.theme_background_color(), sg.theme_background_color()),
               image_filename='./image/HAML.png', image_size=(50, 50), image_subsample=4, border_width=0)],
        [sg.Image(size=(10, 10), filename = './image/HAML.png')],
     [sg.Text("Song library", size=(1270, 1))],
     # [sg.Input(key='-INPUT-UPDATE-SONG-LIB-')],
     [sg.Button('Update', key='-BUTTON-UPDATE-SONG-LIB-')],
     [sg.Text(size=(100, 720), key='-OUTPUT-UPDATE-SONG-LIB-')]],
    key='search_Song-lib_tab'
)  # end of tab search

# search artist name tab
searchArtistTab = sg.Tab(
    'Artists',
    [[sg.Text("Search artist")],
     [sg.Input(key='-INPUT-SEARCH-ARTIST-')],
     [sg.Button('search', key='-BUTTON-SEARCH-ARTIST-')],
     [sg.Text(size=(100, 700), key='-OUTPUT-SEARCH-ARTIST-')]],
    key='search_Artist_tab'
)  # end of tab search

# to be replaced by a nested tab group
deleteTab = sg.Tab(
    'Delete',
    [[sg.TabGroup(
        [[
            deleteTableRecord,
            deleteTableArtist,
            # deleteTableMusician,
            deleteTableAlbum,
            deleteTableSong,
            # deleteTableContains,
            deleteTableMade,
            deleteTableRating
        ]],
        key='tabgroupDelete',
        enable_events=True
    )  # end of TabGroup
    ]],
    #[[sg.Text("Delete something")],
    # [sg.Input(key='-INPUT-DElETE-')],
    # [sg.Button('delete')]],
    key='delete_tab'
)  # end of tab delete

updateTab = sg.Tab(
    'Edit',
    [[sg.TabGroup(
        [[
            updateTableRecord,
            # updateTablePublishes,  # ?
            updateTableArtist,
            #updateTableMusician,
            # createTablePlayed,
            updateTableAlbum,
            updateTableSong,
            # createTableContains,  # ?
            updateTableMade,
            updateTableRating
        ]],
        key='tabgroupUpdate',
        enable_events=True
    )  # end of TabGroup
    ]],

    key='update_tab'

) 


libTab = sg.Tab(
    'Library',
    [[sg.TabGroup(
        [[
            libTableRecord,
            libTableArtist,
            libTableAlbum,
            libTableSong,
            libTableMade,
            libTableRating
        ]],
        key='tabgrouplib',
        enable_events=True
    )  # end of TabGroup
    ]],

    key='lib_tab'

)  # end of tab create



# to be replaced by a nested tab group
createTab = sg.Tab(
    'Add',
    [[sg.TabGroup(
        [[
            createTableRecord,
           # createTablePublishes,  # ?
            createTableArtist,
            #createTableMusician,
           # createTablePlayed,
            createTableAlbum,
            createTableSong,
            #createTableContains,  # ?
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
            libraryTab,

            createTab,  # to be replaced by a tab with tab groups

            updateTab,

            deleteTab,  # to be replaced by a tab with tab groups

            tabgroupSearch,
           
            libTab

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
        temp = db.searchSong
        window['-OUTPUT-SEARCH-ARTIST-'].update(temp)

        str1 = ""


    elif event == '-BUTTON-SEARCH-SONG-':
        temp = db.searchSong(values['-INPUT-SEARCH-SONG-'])
        str1 = ""
        
        window['-OUTPUT-SEARCH-SONG-'].update(temp)

        # window['-OUTPUT-SEARCH-SONG-'].update(values['-INPUT-SEARCH-SONG-'])


def update():
    temp = db.getAllSongs()
    str1 = ""

    songList = db.getAllSongs()
    window.Element('-SONG-L05-').Update(values = songList)

    if temp == "Failed to fetch library":
        window['-OUTPUT-SEARCH-ARTIST-'].update(temp)


update
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
