import PySimpleGUI as sg

### #### #### #### #### #### #### #### #### ###
#            FEELING LUCKY TABLE TABS         #
### #### #### #### #### #### #### #### #### ###


class FeelingLuckyTab:
    def __init__(self, db):
        self.db = db
        self.albumNameList = self.db.allAlbumName()
        self.artistNameList = self.db.allArtistName()
        self.songNameList = self.db.allSongName()
        self.bandNameList = self.db.allBandName()
        self.instrumentList = self.db.allInstName()

    def updateLists(self):
        self.albumNameList = self.db.allAlbumName()
        self.artistNameList = self.db.allArtistName()
        self.songNameList = self.db.allSongName()
        self.bandNameList = self.db.allBandName()
        self.instrumentList = self.db.allInstName()

    def feelingLuckyTabGUI(self):

        flArtistBySongName = sg.Tab(
            'Artists',
            [[sg.Text("Search Artist by Song Name")],
             [sg.Input(key='-INPUT-ARTIST-F01-')],
             [sg.Button('search', key='-BUTTON-ARTIST-F01-')],
             [sg.Table(values=[['                        ', '                        ', '                        ']], headings=[
                 'Artist Name', 'Age', 'Known For'], key='-TABLE-ARTIST-F01-', enable_events=True, size=(1220, 120))]
             ],
            key='F01'
        )

        yearList = list(range(2021, 999, -1))
        flSongByYearAndArtist = sg.Tab(
            'Songs',
            [[sg.Text("Search Song by Year and Artist")],
             
             [sg.Text("Release Year"), sg.Combo(yearList, key='-INPUT-YEAR-F02-')],

             [sg.Text("Artist"), sg.Listbox(values=self.artistNameList,
                                            key='-INPUT-ARTIST-F02-', size=(50, 20))],

             #  [sg.Text("Artist"), sg.Input(key='-INPUT-ARTIST-F02-')],
             [sg.Button('search', key='-BUTTON-SONG-F02-')],
             [sg.Table(values=[['                        ', '                        ', '                        ', '                        ', '                        ', '                        ', '                        ', '                        ', '                        ', '                        ']], headings=[
                 'Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                 'Release Year', 'Average Rating', 'Listeners', 'Rating'], key='-TABLE-SONG-F02-', enable_events=True, size=(1220, 120))]
             ],
            key='F02'
        )

        flRecordLabelByAlbumName = sg.Tab(
            'Record Label by Album',
            [[sg.Text("Search Record Label Details by Album")],
             [sg.Text("Album"), sg.Listbox(values=self.albumNameList, key='-INPUT-ALBUM-F03-', size=(50, 20))],
             [sg.Button('search', key='-BUTTON-RECORD-LABEL-F03-')],
             [sg.Table(values=[['                        ', '                        ', '                        ']], headings=['CompanyName', 'Date Established', 'Label Location'], key='-TABLE-RECORD-LABEL-F03-', enable_events=True, size=(1220, 120))],
             ],
            key='F03'
        )

        flRecordLabelBySongName = sg.Tab(
            'Record Label by Song',
            [[sg.Text("Search Record Label Details by Song")],
             [sg.Text("Song"), sg.Listbox(values=self.songNameList, key='-INPUT-SONG-F04-', size=(50, 20))],
             [sg.Button('search', key='-BUTTON-SONG-F04-')],
             [sg.Table(values=[['                        ', '                        ', '                        ', '                        ']], headings=['CompanyName', 'Recent Album', 'Date Established', 'Label Location'], key='-TABLE-RECORD-LABEL-F04-', enable_events=True, size=(1220, 120))],
             ],
            key='F04'
        )

        flRecordLabelByBandName = sg.Tab(
            'Record Label by Band',
            [[sg.Text("Search Record Label Details by Band")],
             [sg.Text("Band"), sg.Listbox(values=self.bandNameList, key='-INPUT-BAND-F05-', size=(50, 20))],
             [sg.Button('search', key='-BUTTON-RECORD-LABEL-F05-')],
             [sg.Table(values=[['                        ', '                        ', '                        ', '                        ']], headings=['CompanyName', 'Recent Album', 'Date Established', 'Label Location'], key='-TABLE-RECORD-LABEL-F05-', enable_events=True, size=(1220, 120))],
             ],
            key='F05'
        )

        flRecordLabelByInstrument = sg.Tab(
            'Record Label by Instrument',
            [[sg.Text("Search Record Label Details by Instrument")],
             [sg.Text("Instrument"), sg.Listbox(values=self.instrumentList, key='-INPUT-INSTRUMENT-F06-', size=(50, 20))],
             [sg.Button('search', key='-BUTTON-RECORD-LABEL-F06-')],
             [sg.Table(values=[['                        ', '                        ', '                        ', '                        ']], headings=['CompanyName', 'Recent Album', 'Date Established', 'Label Location'], key='-TABLE-RECORD-LABEL-F06-', enable_events=True, size=(1220, 120))],
             ],
            key='F06'
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
                    flSongByYearAndArtist,
                    flRecordLabelByAlbumName,
                    flRecordLabelBySongName,
                    flRecordLabelByBandName,
                    flRecordLabelByInstrument
                ]],
                key='tabgroupFeelingLucky',
                enable_events=True
            )  # end of TabGroup
            ]],

            key='feeling_lucky_tab'

        )  # end of tab insights

        self.updateLists()
        return feelingLuckyTab
