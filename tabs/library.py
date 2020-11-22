import PySimpleGUI as sg

### #### #### #### #### #### #### #### #### ###
#               START OF LIB TABS             #
### #### #### #### #### #### #### #### #### ###


class LibraryTab:
    def __init__(self, db):
        self.db = db

    def libraryTabGUI(self):
        libTableRecord = sg.Tab(
            'Record Label',

            [[sg.Text("Records")],
             #  [sg.Table(testlistbox, key = '-RECORD-L01-', size=(1270, 1))]
             [sg.Table(values=self.db.getAllRecordLabels(), headings=[' CompanyName ', ' Date Established ',
                                                                      ' Label Location '], key='-TABLE-L01-', enable_events=True, size=(1220, 35))],
             #[sg.Table(values = [['','','']], headings=[' CompanyName ', ' Date Established ', ' Label Location '], key = '-TABLE-L01-', enable_events=True, size = (1220, 220))]
             [sg.Button('DELETE', key='-DELETE-BUTTON-L01-')]
             ],
            key='L01'
        )  # end of tab Record Label

        libTableArtist = sg.Tab(
            'Artist',
            [[sg.Text("Artists")],
                #[sg.Listbox(testlistbox, key = '-ARTIST-L02-', size = libSize)]
                [sg.Table(values=self.db.getAllArtists(), headings=[' Artist Name ', ' Age ', ' knownfor ',
                                                                    '  Instrument  ', '      Band      '], key='-TABLE-L02-', enable_events=True, size=(1220, 35))],
                #[sg.Table(values =[['','','','','']], headings=[' Artist Name ', ' Age ', ' knownfor ', '  Instrument  ', '      Band      ' ], key = '-TABLE-L02-', enable_events=True, size = (1220, 220))]
                # [sg.Text("Rating"), sg.Slider(range=(0, 5),
                #                               default_value=0,
                #                               size=(25, 10),
                #                               orientation='horizontal',
                #                               font=('Helvetica', 12), key='-RATING-L03-'),
                #  sg.Button('ADD RATING', key='-BUTTON-L03-'), sg.Button('DELETE', key='-DELETE-BUTTON-L03-')]
                [sg.Button('DELETE', key='-DELETE-BUTTON-L02-')]
             ],
            key='L02'
        )

        libTableAlbum = sg.Tab(
            'Album',
            [[sg.Text("Albums")],
                #[sg.Listbox(testlistbox, key = '-ALBUM-L03-', size = libSize)]
                [sg.Table(values=self.db.getAllAlbums(), headings=[' Title ', 'Album Duration',
                                                                   'Cover Art URL', 'Averaqe Rating', 'Number of Listeners', 'User Rating'], key='-TABLE-L03-', enable_events=True, size=(1220, 35))],
                #[sg.Table(values = [['','','']], headings=[ ' Title ', ' Album Duration ', '        Cover Art URL        ' ], key = '-TABLE-L03-', enable_events=True, size = (1220, 220))]
                [sg.Text("Rating"), sg.Slider(range=(0, 5),
                                              default_value=0,
                                              size=(25, 10),
                                              orientation='horizontal',
                                              font=('Helvetica', 12), key='-RATING-L03-'),
                 sg.Button('ADD RATING', key='-BUTTON-L03-'), sg.Button('DELETE', key='-DELETE-BUTTON-L03-')]
             ],
            key='L03'
        )

        libTableSong = sg.Tab(
            'Song',
            [[sg.Text("Songs")],
             [sg.Table(values=self.db.getAllSongs(), headings=['Song Title', 'Album Title', 'Genre', 'Duration', 'Link',
                                                               'Release Year', 'Average Rating', 'Number of Listeners', 'Rating'], key='-TABLE-L04-', enable_events=True, size=(1220, 35))],
             #[sg.Table(values = [['','','','','','']], headings= ['Title', 'Genre', 'Duration', 'Link', 'Release Year', ' Rating '], key = '-TABLE-L04-', enable_events=True, size = (1220, 220))]
             [sg.Text("Rating"), sg.Slider(range=(0, 5),
                                           default_value=0,
                                           size=(25, 10),
                                           orientation='horizontal',
                                           font=('Helvetica', 12), key='-RATING-L04-'),
              sg.Button('ADD RATING', key='-BUTTON-L04-'), sg.Button('DELETE', key='-DELETE-BUTTON-L04-')]
             ],
            key='L04'
        )

        '''
        def libtabUpdater():
            if event == '-L01-':
                libRecord = self.db.getAllRecordLabels()
                window['-TABLE-L01-'].update(values = libRecord)

            elif event == 'L02-':
                libArtist = self.db.getAllArtists()
                window['-TABLE-L02-'].update(values = libArtist)

            elif event == '-L03-':
                libAlbums = self.db.getAllAlbums()
                window['-TABLE-L03-'].update(values = libAlbums)

            elif event == '-L04-':
                #songList = update list using some sql converted into a list
                libSongs = self.db.getAllSongs()
                window['-TABLE-L04-'].update(values = libSongs)
            '''

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
                    # libTableMade,
                    # libTableRating
                ]],
                key='tabgrouplib',
                enable_events=True
            )  # end of TabGroup
            ]],

            key='lib_tab'

        )  # end of tab create

        return libTab
