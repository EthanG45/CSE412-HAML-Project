import PySimpleGUI as sg

### #### #### #### #### #### #### #### #### ###
#            FEELING LUCKY TABLE TABS         #
### #### #### #### #### #### #### #### #### ###


class FeelingLuckyTab:
    def __init__(self, db):
        self.db = db
        self.artistNameList = self.db.allArtistName()

    def updateLists(self):
        self.artistNameList = self.db.allArtistName()

    def feelingLuckyTabGUI(self):

        flArtistBySongName = sg.Tab(
            'Artists',
            [[sg.Text("Search Artist by Song Name")],
             [sg.Input(key='-INPUT-ARTIST-F01-')],
             [sg.Button('search', key='-BUTTON-ARTIST-F01-')],
             [sg.Table(values=[['', '', '']], headings=[
                 'Artist Name', 'Age', 'Known For'], key='-TABLE-ARTIST-F01-', enable_events=True, size=(1220, 120))]
             ],
            key='F01'
        )

        flSongByYearAndArtist = sg.Tab(
            'Songs',
            [[sg.Text("Search Song by Year and Artist")],
             [sg.Text("Year"), sg.Input(key='-INPUT-YEAR-F02-')],

             [sg.Text("Artist"), sg.Listbox(values=self.artistNameList,
                                            key='-INPUT-ARTIST-F02-',  size=(50, 20))],

             #  [sg.Text("Artist"), sg.Input(key='-INPUT-ARTIST-F02-')],
             [sg.Button('search', key='-BUTTON-SONG-F02-')],
             [sg.Table(values=[['', '', '', '', '', '', '', '', '', '']], headings=[
                 'Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                 'Release Year', 'Average Rating', 'Number of Listeners', 'Rating'], key='-TABLE-SONG-F02-', enable_events=True, size=(1220, 120))]
             ],
            key='F02'
        )

        ### #### #### #### #### #### #### #### #### ###
        #          END OF FEELING LUCKY TABLE TABS    #
        ### #### #### #### #### #### #### #### #### ###

        # to be replaced by a nested tab group
        feelingLuckyTab = sg.Tab(
            'Feeling Lucky',
            [[sg.TabGroup(
                [[
                    flArtistBySongName,
                    flSongByYearAndArtist
                ]],
                key='tabgroupFeelingLucky',
                enable_events=True
            )  # end of TabGroup
            ]],

            key='feeling_lucky_tab'

        )  # end of tab insights

        self.updateLists()
        return feelingLuckyTab
