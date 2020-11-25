import PySimpleGUI as sg


class SearchTab:
    def __init__(self, db):
        self.db = db
    '''
    def searchEvents(self, events, window, values):

        if events == '-BUTTON-SEARCH-SONG-':
            value1 = searchTabGUI.values['-INPUT-SEARCH-SONG-']
        window['-TABLE-SEARCH-SONG-'].Update(value1)
    '''

    def searchTabGUI(self):

        tableSize = (1220, 30)

        # # search song by name tab
        searchSongTab = sg.Tab(
            'Songs',
            [[sg.Text("Search Song", size=(1270, 1))],
             [sg.Input(key='-INPUT-SEARCH-SONG-')],
             [sg.Button('search', key='-BUTTON-SEARCH-SONG-')],
             #[sg.Text(size=(100, 720), key='-OUTPUT-SEARCH-SONG-')]
             [sg.Table(values=[['                     ', '                       ', '                    ', '               ', ' ', '                           ', ' ', '  ', '     ', '   ']], headings=[
                 'Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                 'Release Year', 'Average Rating', 'Listeners', 'Rating'], key='-TABLE-SEARCH-SONG-', enable_events=True, size=tableSize, justification="left")],
             [sg.Text("Rating"), sg.Slider(range=(0, 5),
                                           default_value=0,
                                           size=(25, 10),
                                           orientation='horizontal',
                                           font=('Helvetica', 12), key='-RATING-S01-'),
              sg.Button('ADD RATING', key='-BUTTON-RATING-S01-'), sg.Button('UPDATE', key='-UPDATE-BUTTON-S01-'), sg.Button('DELETE', key='-DELETE-BUTTON-S01-')]

             ],
            key='search_Song_tab'
        )  # end of tab search

        '''
        libraryTab = sg.Tab(
            'Library',

            [
                [sg.Button('Restart Song', button_color=(sg.theme_background_color(), sg.theme_background_color()),
                           image_filename='./image/HAML.png', image_size=(50, 50), image_subsample=4, border_width=0)],
                [sg.Image(size=(10, 10), filename='./image/HAML.png')],
                [sg.Text("Song library", size=(1270, 1))],
                # [sg.Input(key='-INPUT-UPDATE-SONG-LIB-')],
                [sg.Button('Update', key='-BUTTON-UPDATE-SONG-LIB-')],
                [sg.Text(size=(100, 720), key='-OUTPUT-UPDATE-SONG-LIB-')]],
            key='search_Song-lib_tab'
        )  # end of tab search
        '''
        # search artist name tab
        searchArtistTab = sg.Tab(
            'Artists',
            [[sg.Text("Search Artist by Name")],
             [sg.Input(key='-INPUT-SEARCH-ARTIST-')],
             [sg.Button('search', key='-BUTTON-SEARCH-ARTIST-')],
             # [sg.Text(size=(100, 700), key='-OUTPUT-SEARCH-ARTIST-')]],
             [sg.Table(values=[['                        ', '                        ', ''                        ]], headings=[
                 '    Artist Name    ', 'Age', '   Known For   '], key='-TABLE-SEARCH-ARTIST-', enable_events=True, size=tableSize, justification="left")],

             [ sg.Button('UPDATE', key='-UPDATE-BUTTON-S02-'),
             sg.Button('DELETE', key='-DELETE-BUTTON-S02-')]
             ],
            key='search_Artist_tab'
        )  # end of tab search

        searchAlbumTab = sg.Tab(
            'Album',
            [[sg.Text("Search Album by Title")],
             [sg.Input(key='-INPUT-SEARCH-ALBUM-')],
             [sg.Button('search', key='-BUTTON-SEARCH-ALBUM-')],
             # [sg.Text(size=(100, 700), key='-OUTPUT-SEARCH-ARTIST-')]],
             [sg.Table(values=[['                        ', '                        ', '                        ']], headings=['       Title       ', 'Album Duraction',
                                                        '   Cover Art URL   '], key='-TABLE-SEARCH-ALBUM-', enable_events=True, size=tableSize, justification="left")],
             [sg.Button('UPDATE', key='-UPDATE-BUTTON-S03-'), 
             sg.Button('DELETE', key='-DELETE-BUTTON-S03-')]
             ],
            key='search_Album_tab'
        )

        searchBandTab = sg.Tab(
            'Band',
            [[sg.Text("Search Bands")],
             [sg.Input(key='-INPUT-SEARCH-BAND-')],
             [sg.Button('search', key='-BUTTON-SEARCH-BAND-')],
             [sg.Table(values=[['                       ', '                     ', '                        ', '                        ']], 
                        headings=['Name', 'Age', 'Instrument', 'Band'], key='-TABLE-SEARCH-BAND-', enable_events=True, size=tableSize, justification="left")],
             [sg.Button('UPDATE', key='-UPDATE-BUTTON-S04-'),
             sg.Button('DELETE', key='-DELETE-BUTTON-S04-')]
             ],
            key='search_BAND_tab'
        )

        searchRecordLabelTab = sg.Tab(
            'Record Label',
            [[sg.Text("Search Record Label by Name")],
             [sg.Input(key='-INPUT-SEARCH-RECORD-')],
             [sg.Button('search', key='-BUTTON-SEARCH-RECORD-')],
             [sg.Table(values=[['                        ', '                        ', '                        ']], 
             headings=['     Company Name     ', ' Date Established ', '   Label Location   '], key='-TABLE-SEARCH-RECORD-', enable_events=True, size=tableSize, justification="left")],
             [sg.Button('UPDATE', key='-UPDATE-BUTTON-S05-'),
                 sg.Button('DELETE', key='-DELETE-BUTTON-S05-') ]
             ],
            key='search_Record_tab'
        )

        # the nested tab inside the Search tab
        searchTab = sg.Tab(
            'Search',
            [[sg.TabGroup(
                [[
                    searchSongTab,
                    searchAlbumTab,
                    searchArtistTab,
                    searchBandTab,
                    searchRecordLabelTab
                ]],
                key='tabgroupSearch',
                enable_events=True
            )  # end of TabGroup
            ]]
        )

        return searchTab

    def addEvents(self, events):
        eventList = [
            ['-BUTTON-SEARCH-SONG-', self.db.searchSong,
                '-INPUT-SEARCH-SONG-', '-TABLE-SEARCH-SONG-']

        ]

        #eventListButton = [()]
        for elem in eventList:
            events.append(elem)
