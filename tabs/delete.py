import PySimpleGUI as sg

### #### #### #### #### #### #### #### #### ###
#            DELETE TABLE TABS                #
### #### #### #### #### #### #### #### #### ###


class DeleteTab:
    def __init__(self, db):
        self.db = db

    def deleteTabGUI(self):
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

        deleteTableArtist = sg.Tab(
            'Artist',
            [[sg.Text("Create a Artist")],
             [sg.Text("Artist Name")],
             [sg.Input(key='-ARTIST-NAME-D02-')],
             [sg.Text("Age")],
             [sg.Input(key='-AGE-D02-')],

             # Musician elements
             [sg.Text("Instrument")],
             [sg.Input(key='-INSTRUMENT-D02-')],
             [sg.Text("band")],
             [sg.Input(key='-BAND-D02-')],

             [sg.Button('DELETE', key='-BUTTON-D02-')],
             [sg.Text(size=(100, 700), key='-OUTPUT-D02-')]],

            key='D02'
        )

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

        daySize = 5
        monthSize = 7
        yearSize = 10

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
             [sg.Text("Day", size=(daySize, 1)), sg.Text("Month", size=(
                 monthSize, 1)), sg.Text("Year", size=(yearSize, 1))],
             [sg.Input(key='-DAY-D05-', size=(daySize, 1)), sg.Input(key='-MONTH-D05-',
                                                                     size=(monthSize, 1)), sg.Input(key='-YEAR-D05-', size=(yearSize, 1))],

             [sg.Button('DELETE', key='-BUTTON-D05-')],
             [sg.Text(size=(100, 700), key='-OUTPUT-D05-')]

             ],
            key='D05'
        )

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
            # [[sg.Text("Delete something")],
            # [sg.Input(key='-INPUT-DElETE-')],
            # [sg.Button('delete')]],
            key='delete_tab'
        )  # end of tab delete

        return deleteTab
