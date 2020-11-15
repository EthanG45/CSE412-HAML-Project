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

        # # search song by name tab
        searchSongTab = sg.Tab(
            'Songs',
            [[sg.Text("Search Song", size=(1270, 1))],
             [sg.Input(key='-INPUT-SEARCH-SONG-')],
             [sg.Button('search', key='-BUTTON-SEARCH-SONG-')],
             #[sg.Text(size=(100, 720), key='-OUTPUT-SEARCH-SONG-')]
             [sg.Table(values=[['', '', '', '', '']], headings=[
                     '  Title  ', '  Genre  ', ' Source Link ', ' releaseYear '], key='-TABLE-SEARCH-SONG-', enable_events=True, size=(1220, 20))]

             ],
            key='search_Song_tab'
        )  # end of tab search

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

        # search artist name tab
        searchArtistTab = sg.Tab(
            'Artists',
            [[sg.Text("Search artist")],
             [sg.Input(key='-INPUT-SEARCH-ARTIST-')],
             [sg.Button('search', key='-BUTTON-SEARCH-ARTIST-')],
             [sg.Text(size=(100, 700), key='-OUTPUT-SEARCH-ARTIST-')]],
            key='search_Artist_tab'
        )  # end of tab search

        # the nested tab inside the Search tab
        searchTab = sg.Tab(
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

        return searchTab

    def addEvents(self, events):
        eventList = [
            ('-BUTTON-SEARCH-SONG-', self.db.searchSong,
                '-INPUT-SEARCH-SONG-', '-TABLE-SEARCH-SONG-')
        ]

        for elem in eventList:
            events.append(elem)
