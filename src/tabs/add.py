import PySimpleGUI as sg
from faker import Faker
fake = Faker()
Faker.seed(2)
### #### #### #### #### #### #### #### #### ###
#            ADD TABLE TABS                   #
### #### #### #### #### #### #### #### #### ###
class AddTab:
    def __init__(self, db):
        self.db = db
        self.albumNameList = self.db.allAlbumName()
        self.artistNameList = self.db.allArtistName()
        self.recordLabelList = self.db.allCompanyName()
        self.instrumentList = self.db.allInstName()
        self.genreList = self.db.allGenre()

    def updateLists(self):
        self.albumNameList = self.db.allAlbumName()
        self.artistNameList = self.db.allArtistName()
        self.recordLabelList = self.db.allCompanyName()
        self.instrumentList = self.db.allInstName()
        self.genreList = self.db.allGenre()

    def addTabGUI(self):
        ageList = []
        locationList = []

        for x in range(155):
            ageList.append(x)

        for x in range(0, 1000):
            locationList.append(fake.city())

        yearList = list(range(2021, 999, -1))

        addTableRecord = sg.Tab(
            'Record Label',

            [[sg.Text("Add a Record Label", size=(1270, 1))],
             [sg.Text("Company Name"), sg.Input(key='-companyName-C01-')],

            [sg.Text("Label Location"), sg.Combo(locationList, key='-labelLocation-C01-')],

             [sg.Text("What album did this record label publish?", size=(1270, 1))],

             # Album elements
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
             [sg.Text("Genre"), sg.Listbox(values=self.genreList, key='-GENRE-C02-', size=(10, 5))],

             [sg.Text("Release Year"), sg.Combo(yearList, key='-RELEASE-YEAR-C02-')],

             [sg.Text("Record Label"), sg.Listbox(values=self.recordLabelList, key='-RECORD-TITLE-C02-', size=(40, 8))],

             [sg.Button('ADD', key='-BUTTON-C02-')],

             [sg.Text(size=(100, 720), key='-OUTPUT-C02-')]

             ],

            key='C02'
        )

        addTableAlbum = sg.Tab(
            'Album',
            [[sg.Text("Add an Album")],

             [sg.Text("Title"), sg.Input(key='-ALBUM-TITLE-C04-')],

             [sg.Text("Add the Album's first song")],
             [sg.Text("Title"), sg.Input(key='-SONG-TITLE-C04-')],
             [sg.Text("Genre"), sg.Listbox(values=self.genreList,
                                           key='-GENRE-C04-', size=(10, 5))],
             [sg.Text("Release Year"), sg.Combo(
                 yearList, key='-RELEASE-YEAR-C04-')],
             [sg.Text("Artist"), sg.Listbox(values=self.artistNameList,
                                            key='-ARTIST-TITLE-C04-', size=(50, 20))],
             [sg.Button('ADD', key='-BUTTON-C04-')],

             [sg.Text(size=(100, 720), key='-OUTPUT-C04-')]

             ],

            key='C04'
        )

        addTableSong = sg.Tab(
            'Song',
            [[sg.Text("Add a song")],
             [sg.Text("Title"), sg.Input(key='-TITLE-C05-')],
             [sg.Text("Genre"), sg.Listbox(values=self.genreList,
                                           key='-GENRE-C05-', size=(10, 10))],
             [sg.Text("Album Title"), sg.Listbox(values=self.albumNameList,
                                                 key='-ALBUM-TITLE-C05-', size=(50, 20))],
             [sg.Text("Release Year"), sg.Combo(
                 yearList, key='-releaseYear-C05-')],

             [sg.Button('ADD', key='-BUTTON-C05-')],

             [sg.Text(size=(100, 720), key='-OUTPUT-C05-')]

             ],
            key='C05'
        )

        ### #### #### #### #### #### #### #### #### ###
        #          END OF ADD TABLE TABS              #
        ### #### #### #### #### #### #### #### #### ###

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
