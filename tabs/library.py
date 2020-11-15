import PySimpleGUI as sg

### #### #### #### #### #### #### #### #### ###
#               START OF LIB TABS             #
### #### #### #### #### #### #### #### #### ###

class LibraryTab:
    def __init__(self, db):
        self.db = db

    def libraryTabGUI(self):
        libTableRecord = sg.Tab(
            'Record',

            [[sg.Text("Records")],
            #  [sg.Table(testlistbox, key = '-RECORD-L01-', size=(1270, 1))]
            [sg.Table(values = self.db.getAllRecordLabels(), headings=[' CompanyName ', ' Date Established ', ' Label Location '], key = '-TABLE-L01-', enable_events=True, size = (1220, 120))]
            #  [sg.Table(values = db., headings= ['Title', 'Genre', 'Duration', 'Link', 'Release Year'], key = '-SONG-L05-', enable_events=True)]
            ],
            key='L01'
        )  # end of tab Record

        libTableArtist = sg.Tab(
            'Artist',
            [[sg.Text("Artists")],
                #[sg.Listbox(testlistbox, key = '-ARTIST-L02-', size = libSize)]
                [sg.Table(values = self.db.getAllArtists(), headings=[' Artist Name ', ' Age ', ' knownfor ' ], key = '-TABLE-L02-', enable_events=True, size = (1220, 120))]
            ],
            key='L02'
        )

        libTableAlbum = sg.Tab(
            'Album',
            [[sg.Text("Albums")],
                #[sg.Listbox(testlistbox, key = '-ALBUM-L04-', size = libSize)]
                [sg.Table(values = self.db.getAllAlbums(), headings=[' Album Duration ', ' Title ', ' Cover Art URL ' ], key = '-TABLE-L04-', enable_events=True, size = (1220, 120))]
            ],
            key='L04'
        )

        libTableSong = sg.Tab(
            'Song',
            [[sg.Text("Songs")],
            [sg.Table(values = self.db.getAllSongs(), headings= ['Title', 'Genre', 'Duration', 'Link', 'Release Year', ' Rating '], key = '-TABLE-L05-', enable_events=True, size = (1220, 20))]
            ],
            key='L05'
        )


        libTableMade = sg.Tab(
            'Made', 
            [[sg.Text("Made")]
                #[sg.Table(testlistbox, key = '-MADE-L06-', size = libSize)]
                #[sg.Table(values = db.getAllAlbums(), headings=[' knownFor '], key = '-TABLE-L06-', enable_events=True, size = (710, 120))]
            ],
            key='L06'
        )

        libTableRating = sg.Tab(
            'Rating',
            [[sg.Text("Ratings")]
                #[sg.Table(testlistbox, key = '-RATING-L07-', size = libSize)]
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
                songList = self.db.getAllSongs()
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

        libTab = sg.Tab(
            'Library',
            [[sg.TabGroup(
                [[
                    libTableRecord,
                    libTableArtist,
                    libTableAlbum,
                    libTableSong
                    #libTableMade,
                    #libTableRating
                ]],
                key='tabgrouplib',
                enable_events=True
            )  # end of TabGroup
            ]],

            key='lib_tab'

        )  # end of tab create

        return libTab
