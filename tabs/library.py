import PySimpleGUI as sg

### #### #### #### #### #### #### #### #### ###
#               START OF LIB TABS             #
### #### #### #### #### #### #### #### #### ###
class LibraryTab:
    def __init__(self, db):
        self.db = db

    def libraryTabGUI(self):

        libTableSize = (1220, 30)

        libTableRecord = sg.Tab(
            'Record Label',

            [[sg.Text("Records")],
             [sg.Table(values=self.db.getAllRecordLabels(), headings=['CompanyName', 'Recent Album', 'Date Established',
                                                                      'Label Location'], key='-TABLE-L01-', enable_events=True, size=libTableSize, justification="left")],
            [sg.Button('UPDATE', key='-UPDATE-BUTTON-L01-'),
             sg.Button('DELETE', key='-DELETE-BUTTON-L01-')]
             ],
            key='L01'
        )  # end of tab Record Label

        libTableArtist = sg.Tab(
            'Artist',
            [[sg.Text("Artists")],
                [sg.Table(values=self.db.getAllArtists(), headings=[' Artist Name ', ' Age ', ' knownfor ',
                                                                    '  Instrument  ', '      Band      '], key='-TABLE-L02-', enable_events=True, size=libTableSize, justification="left")],
                [ sg.Button('UPDATE', key='-UPDATE-BUTTON-L02-'),
                sg.Button('DELETE', key='-DELETE-BUTTON-L02-')]
             ],
            key='L02'
        )

        libTableAlbum = sg.Tab(
            'Album',
            [[sg.Text("Albums")],
                [sg.Table(values=self.db.getAllAlbums(), headings=['Title', 'Album Duration',
                                                                   'Cover Art URL', 'Averaqe Rating', 'Listeners', 'User Rating'], key='-TABLE-L03-', enable_events=True, size=libTableSize, justification="left")],
                
                [sg.Button('UPDATE', key='-UPDATE-BUTTON-L03-'),
                sg.Button('DELETE', key='-DELETE-BUTTON-L03-')]
              
            ],
            key='L03'
        )

        libTableSong = sg.Tab(
            'Song',
            [[sg.Text("Songs")],

             [sg.Table(values=self.db.getAllSongs(), headings=['Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                                                               'Release Year', 'Average Rating', 'Listeners', 'Rating'], key='-TABLE-L04-', enable_events=True, size=libTableSize, justification="left")],
             [sg.Text("Rating"), sg.Slider(range=(0, 5),
                                           default_value=0,
                                           size=(25, 10),
                                           orientation='horizontal',
                                           font=('Helvetica', 12), key='-RATING-L04-'),
              sg.Button('ADD RATING', key='-BUTTON-L04-'), 
                sg.Button('UPDATE', key='-UPDATE-BUTTON-L04-'), 
                sg.Button('DELETE', key='-DELETE-BUTTON-L04-')]
             ],
            key='L04'
        )

        ### #### #### #### #### #### #### #### #### ###
        #                END OF LIB TABS              #
        ### #### #### #### #### #### #### #### #### ###

        libTab = sg.Tab(
            'Library',
            [[sg.TabGroup(
                [[
                    libTableSong,
                    libTableAlbum,
                    libTableArtist,
                    libTableRecord
                ]],
                key='tabgrouplib',
                enable_events=True
            )  # end of TabGroup
            ]],

            key='lib_tab'

        )  # end of tab

        return libTab
