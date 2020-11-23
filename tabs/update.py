import PySimpleGUI as sg

### #### #### #### #### #### #### #### #### ###
#           START UPDATE TABLE TABS           #
### #### #### #### #### #### #### #### #### ###


class UpdateTab:
    def __init__(self, db):
        self.db = db

    def updateTabGUI(self):
        updateTableRecord = sg.Tab(
            'Record Label',

            [[sg.Text("Update A Table Record Label", size=(1270, 1))],
             [sg.Text("Company Name"), sg.Input(key='-companyName-U01-')],
             [sg.Text("Date Established"), sg.Input(key='-dateEstablished-U01-')],
             [sg.Text("Label Location"), sg.Input(key='-labelLocation-U01-')],
             [sg.Text("Record Label Id"), sg.Input(key='-recordLabelId-U01-')],
             [sg.Button('DELETE', key='-BUTTON-U01-')],
             [sg.Text(size=(100, 700), key='-OUTPUT-U01-')]],
            key='U01'
        )  # end of tab Record Label

        updateTableArtist = sg.Tab(
            'Artist',
            [[sg.Text("Update an Artist")],
             # Artist Elements
             [sg.Text("Artist Name"), sg.Input(key='-ARTIST-NAME-U02-')],
             [sg.Text("Age"), sg.Input(key='-AGE-U02-')],

             # Musician elements
             [sg.Text("Instrument"), sg.Input(key='-INSTRUMENT-U02-')],
             [sg.Text("band"), sg.Input(key='-BAND-U02-')],

             [sg.Button('DELETE', key='-BUTTON-U02-')],
             [sg.Text(size=(100, 700), key='-OUTPUT-U02-')]],

            key='U02'
        )

        updateTableAlbum = sg.Tab(
            'Album',
            [[sg.Text("Update an Album")],

             [sg.Text("Album Duration"), sg.Input(key='-ALBUM-DURATION-U04-')],
             [sg.Text("Title"), sg.Input(key='-TITLE-U04-')],
             [sg.Text("Cover Art URL"), sg.Input(key='-COVER ART URL-U04-')],

             [sg.Button('DELETE', key='-BUTTON-U04-')],
             [sg.Text(size=(100, 700), key='-OUTPUT-U04-')]

             ],

            key='U04'
        )

        daySize = 5
        monthSize = 7
        yearSize = 10

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

             [sg.Text("Day", size=(daySize, 1)), sg.Text("Month", size=(
                 monthSize, 1)), sg.Text("Year", size=(yearSize, 1))],
             [sg.Input(key='-DAY-U05-', size=(daySize, 1)), sg.Input(key='-MONTH-U05-',
                                                                     size=(monthSize, 1)), sg.Input(key='-YEAR-U05-', size=(yearSize, 1))],

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

        updateTab = sg.Tab(
            'Edit',
            [[sg.TabGroup(
                [[
                    updateTableRecord,
                    # updateTablePublishes,  # ?
                    updateTableArtist,
                    # updateTableMusician,
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

        return updateTab

    def updateRecordLabelGUI(self):
        layout = [[sg.Text('Company Name'),
                   sg.Input(size=(10, 1), key='-COMPANY-NAME-U01-')],
                  [sg.Text('Label Location'),
                   sg.Input(size=(10, 1), key='-LABEL-LOCATION-U01-')],
                  [sg.Button('UPDATE', key='-RECORD-LABEL-BUTTON-U01-')]
                  ]

        return layout

    def updateArtistGUI(self):

        layout = [[sg.Text('Age'),
                   sg.Input(size=(10, 1), key='-AGE-U01-')],
                  [sg.Button('UPDATE', key='-ARTIST-BUTTON-U01-')]
                  ]

        return layout

    def updateAlbumGUI(self):

        layout = [[sg.Text('Title'),
                   sg.Input(size=(10, 1), key='-TITLE-U03-')],
                  [sg.Text('Duration'),
                   sg.Input(size=(10, 1), key='-DURATION-U03-')],
                  [sg.Button('UPDATE', key='-ALBUM-BUTTON-U03-')]
                  ]

        return layout

    def updateSongGUI(self):

        layout = [[sg.Text('Title'),
                   sg.Input(size=(10, 1), key='-TITLE-U04-')],
                  [sg.Text('Duration'),
                   sg.Input(size=(10, 1), key='-DURATION-U04-')],
                  [sg.Button('UPDATE', key='-ALBUM-BUTTON-U01-')]
                  ]

        return layout
