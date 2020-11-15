import PySimpleGUI as sg

### #### #### #### #### #### #### #### #### ###
#            CREATE TABLE TABS                #
### #### #### #### #### #### #### #### #### ###


class CreateTab:
    def __init__(self, db):
        self.db = db

    def createTabGUI(self):
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

        createTableArtist = sg.Tab(
            'Artist',

            [[sg.Text("Create a Artist")],
             [sg.Text("Artist Name")],
             [sg.Input(key='-ARTIST-C02-')],
             [sg.Text("Age")],
             [sg.Input(key='-AGE-C02-')],

             # Musician elements
             [sg.Text("Instrument")],
             [sg.Input(key='-INSTRUMENT-C02-')],
             [sg.Text("band")],
             [sg.Input(key='-BAND-C02-')],

             [sg.Button('CREATE', key='-BUTTON-C02-')],
             [sg.Text(size=(100, 720), key='-OUTPUT-C02-')]],
            key='C02'
        )

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
             [sg.Text("Day", size=(daySize, 1)), sg.Text("Month", size=(
                 monthSize, 1)), sg.Text("Year", size=(yearSize, 1))],
             [sg.Input(key='-DAY-C05-', size=(daySize, 1)),     sg.Input(key='-MONTH-C05-',
                                                                         size=(monthSize, 1)),     sg.Input(key='-YEAR-C05-', size=(yearSize, 1))],

             # [sg.Input(key='-RELEASE-YEAR-C07-')],
             [sg.Button('CREATE', key='-BUTTON-C05-')],

             [sg.Text(size=(100, 720), key='-OUTPUT-C05-')]

             ],
            key='C05'
        )

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

        # to be replaced by a nested tab group
        createTab = sg.Tab(
            'Create',
            [[sg.TabGroup(
                [[
                    createTableRecord,
                    # createTablePublishes,  # ?
                    createTableArtist,
                    # createTableMusician,
                    # createTablePlayed,
                    createTableAlbum,
                    createTableSong,
                    # createTableContains,  # ?
                    createTableMade,
                    createTableRating
                ]],
                key='tabgroupCreate',
                enable_events=True
            )  # end of TabGroup
            ]],

            key='create_tab'

        )  # end of tab create

        return createTab

    #def addEvents
