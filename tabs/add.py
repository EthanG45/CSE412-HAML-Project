import PySimpleGUI as sg

### #### #### #### #### #### #### #### #### ###
#            ADD TABLE TABS                #
### #### #### #### #### #### #### #### #### ###


class AddTab:
    def __init__(self, db):
        self.db = db
        self.albumNameList = self.db.allAlbumName()
        self.artistNameList = self.db.allArtistName()
        self.recordLabelList = self.db.allCompanyName()
        self.instrumentList = self.db.allInstName()
        # print(self.albumNameList[0][0])
        # self.albumNameList = list(map(str, self.albumNameList))

    def updateLists(self):
        # TODO THis doesnt auto update properly. just get it in gui.py and pass as an arg i think
        self.albumNameList = self.db.allAlbumName()
        self.artistNameList = self.db.allArtistName()
        self.recordLabelList = self.db.allCompanyName()
        self.instrumentList = self.db.allInstName()
        # self.recordLabelList = self.db.allRecordLabel()
        # self.albumNameList = list(map(str, self.albumNameList))

    def addTabGUI(self):
        ageList = []

        for x in range(155):
            ageList.append(x)

        releaseYear = []

        yearList = list(range(2021, 999, -1))

        for x in range(1000, 2021):
            releaseYear.insert(0, x)

        genre = ["Rap", "Rock", "Country", "Hip Hop", "Soundtrack", "EDM", "Metal", "Heavy Metal", "Pop"]

        addTableRecord = sg.Tab(
            'Record Label',

            [[sg.Text("Add a Record Label", size=(1270, 1))],
             [sg.Text("Company Name"), sg.Input(key='-companyName-C01-')],
             [sg.Text("Label Location"), sg.Input(key='-labelLocation-C01-')],
             [sg.Text("What album did this record label publish?", size=(1270, 1))],
             # Album elements
             #  [sg.Text("Title"), sg.Input(key='-TITLE-C02-')],
             [sg.Text("Title"), sg.Listbox(values=self.albumNameList,
                                           key='-TITLE-C01-', size=(50, 20))],
             [sg.Text("Date Established"), sg.Input(key='-dateEstablished-C01-', size=(20, 1)),
              sg.CalendarButton('Date Picker', close_when_date_chosen=True, format='%Y-%m-%d', target='-dateEstablished-C01-', no_titlebar=False, key='Calendar-C01')],

             [sg.Button('ADD', key='-BUTTON-C01-')],
             [sg.Text(size=(100, 720), key='-OUTPUT-C01-')]],
            key='C01'
        )  # end of tab Record Label

        addTableArtist = sg.Tab(
            'Artist',

            [[sg.Text("Add an Artist", size=(1270, 1))],

             # Artist elements
             [sg.Text("Artist Name"), sg.Input(key='-ARTIST-C02-')],
             [sg.Text("Age"), sg.Slider(range=(1, 155),
                                        default_value=42,
                                        size=(40, 15),
                                        orientation='horizontal',
                                        font=('Helvetica', 12), key='-AGE-C02-')],
             # Musician elements
             [sg.Text("Instrument"), sg.Listbox(values=self.instrumentList, key='-INSTRUMENT-C02-', size=(10, 5))],
             [sg.Text("Band Name"), sg.Input(key='-BAND-C02-')],

             # Album Elements
             [sg.Text("What album did this artist make?", size=(1270, 1))],

             [sg.Text("Add an Album")],

             [sg.Text("Title"), sg.Input(key='-ALBUM-TITLE-C02-')],

             [sg.Text("Add the Album's first song")],
             [sg.Text("Title"), sg.Input(key='-SONG-TITLE-C02-')],
             [sg.Text("Genre"), sg.Listbox(values=genre, key='-GENRE-C02-', size=(10, 5))],

             [sg.Text("Release Year"), sg.Combo(yearList, key='-RELEASE-YEAR-C02-')],

             [sg.Text("Record Label"), sg.Listbox(values=self.recordLabelList, key='-RECORD-TITLE-C02-', size=(50, 20))],

             [sg.Button('ADD', key='-BUTTON-C02-')],

             [sg.Text(size=(100, 720), key='-OUTPUT-C02-')]




             ],

            key='C02'
        )

        addTableAlbum = sg.Tab(
            'Album',
            [[sg.Text("Add an Album")],

             [sg.Text("Title"), sg.Input(key='-ALBUM-TITLE-C04-')],

             #  [sg.Text("Search Song to add to album", size=(1220, 1))],

             #  [sg.Input(key='-INPUT-SEARCH-SONG-C04-'),
             #  sg.Button('search', key='-BUTTON-SEARCH-SONG-C04-')],

             #  [sg.Table(values=[['', '', '', '', '', '']], headings=[
             #          '  Title  ', '  Genre  ', '     Source Link     ',
             #           ' releaseYear ', ' Rating Count ', ' Average Rating '],
             #           key='-TABLE-SEARCH-SONG-C04-', enable_events=True, size=(1220, 20))],

             #  [sg.Button('ADD SONG', key='-ADD-SONG-C04-'),
             #  sg.Button('ADD', key='-BUTTON-C04-')],

             [sg.Text("Add the Album's first song")],
             [sg.Text("Title"), sg.Input(key='-SONG-TITLE-C04-')],
             [sg.Text("Genre"), sg.Listbox(values=genre,
                                           key='-GENRE-C04-', size=(10, 5))],
             #  layout = [[sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6))]]
             # [sg.Text("Source Link"), sg.Input(key='-SOURCE-C05-')],

             [sg.Text("Release Year"), sg.Combo(
                 yearList, key='-RELEASE-YEAR-C04-')],

             [sg.Text("Artist"), sg.Listbox(values=self.artistNameList,
                                            key='-ARTIST-TITLE-C04-', size=(50, 20))],
             # [sg.Text("Day", size=(daySize, 1)), sg.Text("Month", size=(monthSize, 1)), sg.Text("Year", size=(yearSize, 1))],
             # [sg.Input(key='-DAY-C05-', size=(daySize, 1)), sg.Input(key='-MONTH-C05-',  size=(monthSize, 1)), sg.Input(key='-YEAR-C05-', size=(yearSize, 1))],

             #   [sg.Text("Age"), sg.Combo(ageList,size=(10, 1), key='-AGE-C02-')],
             # [sg.Text("Release Year"), sg.Input(key='-releaseYear-C05-', size=(20, 1)),
             # sg.CalendarButton('Date Picker', close_when_date_chosen=True, format='%Y-%m-%d', target='-releaseYear-C05-', no_titlebar=False, key='Calendar-C05')],

             # [sg.Input(key='-RELEASE-YEAR-C07-')],
             [sg.Button('ADD', key='-BUTTON-C04-')],

             [sg.Text(size=(100, 720), key='-OUTPUT-C04-')]

             ],


            # [sg.Table

            # ],

            key='C04'
        )

        addTableSong = sg.Tab(
            'Song',
            [[sg.Text("Add a song")],
             [sg.Text("Title"), sg.Input(key='-TITLE-C05-')],
             [sg.Text("Genre"), sg.Listbox(values=genre,
                                           key='-GENRE-C05-', size=(10, 10))],
             [sg.Text("Album Title"), sg.Listbox(values=self.albumNameList,
                                                 key='-ALBUM-TITLE-C05-', size=(50, 20))],
             #  layout = [[sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6))]]
             # [sg.Text("Source Link"), sg.Input(key='-SOURCE-C05-')],

             [sg.Text("Release Year"), sg.Combo(
                 yearList, key='-releaseYear-C05-')],


             # [sg.Text("Day", size=(daySize, 1)), sg.Text("Month", size=(monthSize, 1)), sg.Text("Year", size=(yearSize, 1))],
             # [sg.Input(key='-DAY-C05-', size=(daySize, 1)), sg.Input(key='-MONTH-C05-',  size=(monthSize, 1)), sg.Input(key='-YEAR-C05-', size=(yearSize, 1))],

             #   [sg.Text("Age"), sg.Combo(ageList,size=(10, 1), key='-AGE-C02-')],
             # [sg.Text("Release Year"), sg.Input(key='-releaseYear-C05-', size=(20, 1)),
             # sg.CalendarButton('Date Picker', close_when_date_chosen=True, format='%Y-%m-%d', target='-releaseYear-C05-', no_titlebar=False, key='Calendar-C05')],

             # [sg.Input(key='-RELEASE-YEAR-C07-')],
             [sg.Button('ADD', key='-BUTTON-C05-')],

             [sg.Text(size=(100, 720), key='-OUTPUT-C05-')]

             ],
            key='C05'
        )

        # addTableMade = sg.Tab(
        #     'Made',
        #     [[sg.Text("-----")],
        #      [sg.Text("Known For?"), sg.Input(key='-KNOWN-FOR-C06-')],

        #      [sg.Button('ADD', key='-BUTTON-C06-')],
        #      [sg.Text(size=(100, 720), key='-OUTPUT-C06-')]
        #      ],
        #     key='C06'
        # )

        # addTableRating = sg.Tab(
        #     'Rating',
        #     [[sg.Text("add a rating")],
        #      [sg.Text("Number Of Rating")],
        #      [sg.Input(key='-NUM-OF-RATING-C07-')],
        #      [sg.Text("Average Rating")],
        #      [sg.Input(key='-AVERAGE-RATING-C07-')],
        #      [sg.Text("User Rating")],
        #      [sg.Input(key='-USER-RATING-C07-')],

        #      [sg.Button('ADD', key='-BUTTON-C07-')],
        #      [sg.Text(size=(100, 720), key='-OUTPUT-C07-')]
        #      ],
        #     key='C07'
        # )

        ### #### #### #### #### #### #### #### #### ###
        #          END OF ADD TABLE TABS              #
        ### #### #### #### #### #### #### #### #### ###

        # to be replaced by a nested tab group
        addTab = sg.Tab(
            'Add',
            [[sg.TabGroup(
                [[
                    addTableSong,
                    addTableAlbum,
                    addTableArtist,
                    addTableRecord
                ]],
                key='tabgroupAdd',
                enable_events=True
            )  # end of TabGroup
            ]],

            key='add_tab'

        )  # end of tab add

        return addTab
