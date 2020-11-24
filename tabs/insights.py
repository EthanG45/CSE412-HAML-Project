import PySimpleGUI as sg
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

### #### #### #### #### #### #### #### #### ###
#            INSIGHTS TABLE TABS              #
### #### #### #### #### #### #### #### #### ###

from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.pyplot import figure

class InsightsTab:
    def __init__(self, db):
        self.db = db
        # self.fig, self.ax = plt.subplots()
        self.top10SongByAverage = self.db.topTenSongsByAverage()
        self.top10SongByUser = self.db.topTenSongsByUser()
        self.top10AlbumByAverage = self.db.topTenAlbumsByAverage()
        self.top10AlbumByUser = self.db.topTenAlbumsByUser()
        self.top10WorstSongByAverage = self.db.topTenSongsByAverageWorst()
        self.top10WorstSongByUser = self.db.topTenSongsByUserWorst()
        self.top10WorstAlbumByAverage = self.db.topTenAlbumsByAverageWorst()
        self.top10WorstAlbumByUser = self.db.topTenAlbumsByUserWorst()

    def updateLists(self):
        self.top10SongByAverage = self.db.topTenSongsByAverage()
        self.top10SongByUser = self.db.topTenSongsByUser()
        self.top10AlbumByAverage = self.db.topTenAlbumsByAverage()
        self.top10AlbumByUser = self.db.topTenAlbumsByUser()
        self.top10WorstSongByAverage = self.db.topTenSongsByAverageWorst()
        self.top10WorstSongByUser = self.db.topTenSongsByUserWorst()
        self.top10WorstAlbumByAverage = self.db.topTenAlbumsByAverageWorst()
        self.top10WorstAlbumByUser = self.db.topTenAlbumsByUserWorst()


    def insightsTabGUI(self):

        top10Songs = sg.Tab(
            'Top 10 Songs',

            # TODO table sizing is weird
            [
                [sg.Text("Top 10 Songs by Average Rating")],
                [sg.Table(values=self.top10SongByAverage, headings=['Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                                                                    'Release Year', 'Average Rating', 'Listeners', 'Rating'], key='-AVG-TABLE-I01-', enable_events=True, size=(1220, 10), justification="left")],


                [sg.Text("Top 10 Songs by User Rating")],
                [sg.Table(values=self.top10SongByUser, headings=['Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                                                                 'Release Year', 'Average Rating', 'Listeners', 'Rating'], key='-USER-TABLE-I01-', enable_events=True, size=(1220, 10), justification="left")]
            ],
            key='I01'
        )  # end of tab Record Label

        top10SongsGraph = sg.Tab(
            'Top 10 Songs Graph',
            [
                [sg.Text("Distribution of Genres for Top 10 Songs by User Rating")],
                [sg.Canvas(key='-ALBUM-CANVAS-IO-?-')],
                [sg.Canvas(key='-SONG-CANVAS-IO-?-')],
            ],
            key='I05'
        )  # end of tab Record Label

        top10Albums = sg.Tab(
            'Top 10 Albums',
            # TODO table sizing is weird
            [[sg.Text("Top 10 Albums by Average Rating")],
             [sg.Table(values=self.top10AlbumByAverage, headings=['Title', 'Album Duration',
                                                                  'Cover Art URL', 'Averaqe Rating', 'Listeners', 'User Rating'], key='-AVG-TABLE-I02-', enable_events=True, size=(1220, 10), justification="left")],
             [sg.Text("Top 10 Albums by User Rating")],
             [sg.Table(values=self.top10AlbumByUser, headings=['Title', 'Album Duration',
                                                               'Cover Art URL', 'Averaqe Rating', 'Listeners', 'User Rating'], key='-USER-TABLE-I02-', enable_events=True, size=(1220, 10), justification="left")]
             ],
            key='I02'
        )  # end of tab Record Label

        top10AlbumsGraph = sg.Tab(
            'Top 10 Songs Graph',
            [
                [sg.Text("Distribution of Genres for Top 10 Songs by User Rating")],
                [sg.Canvas(key='-CANVAS-')],
                [sg.Canvas(key='-SONG-CANVAS-IO-?-')],
                [sg.Canvas(key='-CANVAS-3-')],
            ],
            key='I05'
        )  # end of tab Record Label

        top10WorstSongs = sg.Tab(
            'Top 10 Worst Songs',

            # TODO table sizing is weird
            [[sg.Text("Top 10 Worst Songs by Average Rating")],
             [sg.Table(values=self.top10WorstSongByAverage, headings=['Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                                                                      'Release Year', 'Average Rating', 'Listeners', 'Rating'], key='-AVG-TABLE-I03-', enable_events=True, size=(1220, 10), justification="left")],
             [sg.Text("Top 10 Worst Songs by User Rating")],
             [sg.Table(values=self.top10WorstSongByUser, headings=['Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                                                                   'Release Year', 'Average Rating', 'Listeners', 'Rating'], key='-USER-TABLE-I03-', enable_events=True, size=(1220, 10), justification="left")]
             ],
            key='I03'
        )  # end of tab Record Label

        top10WorstAlbums = sg.Tab(
            'Top 10 Worst Albums',
            # TODO table sizing is weird
            [[sg.Text("Top 10 Worst Albums by Average Rating")],
             [sg.Table(values=self.top10WorstAlbumByAverage, headings=['Title', 'Album Duration',
                                                                       'Cover Art URL', 'Averaqe Rating', 'Listeners', 'User Rating'], key='-AVG-TABLE-I04-', enable_events=True, size=(1220, 10), justification="left")],
             [sg.Text("Top 10 Worst Albums by User Rating")],
             [sg.Table(values=self.top10WorstAlbumByUser, headings=['Title', 'Album Duration',
                                                                    'Cover Art URL', 'Averaqe Rating', 'Listeners', 'User Rating'], key='-USER-TABLE-I04-', enable_events=True, size=(1220, 10), justification="left")]
             ],
            key='I04'
        )  # end of tab Record Label

        ### #### #### #### #### #### #### #### #### ###
        #          END OF INSIGHTS TABLE TABS           #
        ### #### #### #### #### #### #### #### #### ###

        # to be replaced by a nested tab group
        insightsTab = sg.Tab(
            'Insights',
            [[sg.TabGroup(
                [[
                    top10Songs,
                    top10SongsGraph,
                    top10Albums,
                    top10WorstSongs,
                    top10WorstAlbums
                ]],
                key='tabgroupInsights',
                enable_events=True
            )  # end of TabGroup
            ]],

            key='insights_tab'

        )  # end of tab insights

        return insightsTab

    def topTenAlbumsByUserPieFigure(self, canvas, db):
        figure, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
        listData = []
        listLabel = []

        for elem in db.topTenAlbumsByUser():
            listData.append(elem[4])
            listLabel.append(elem[0])

        ax.pie(listData,labels=listLabel, autopct='%1i%%',shadow=True)
        ax.set_title("Number of Listeners per Title")

        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)

    def topTenSongsByUserPieFigure(self, canvas, db):
        figure, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
        label = ['Country', 'EDM', 'Heavy Metal', 'Hip Hop', 'Metal', 'Pop', 'Rap', 'Rock', 'Soundtrack']
        data = {'Country': 0, 'EDM': 0, 'Heavy Metal': 0,'Hip Hop': 0, 'Metal': 0, 'Pop': 0, 'Rap': 0, 'Rock': 0,'Soundtrack': 0}
        listData = []
        listLabel = []

        for elem in db.topTenSongsByUser():
            res = elem[3]
            data[res] = data[res] + 1.

        for i in label:
            for elem in data:
                if i == elem and data[elem] != 0.:
                    listData.append(data[elem])
                    listLabel.append(elem)
                    
        ax.pie(listData,labels=listLabel, autopct='%1i%%',shadow=True)
        ax.set_title("Genre Distribution within Top 10 Songs by User Rating")

        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    
    def topTenSongsByAveragePieFigure(self, canvas, db):
        figure, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
        label = ['Country', 'EDM', 'Heavy Metal', 'Hip Hop', 'Metal', 'Pop', 'Rap', 'Rock', 'Soundtrack']
        data = {'Country': 0, 'EDM': 0, 'Heavy Metal': 0,'Hip Hop': 0, 'Metal': 0, 'Pop': 0, 'Rap': 0, 'Rock': 0,'Soundtrack': 0}
        listData = []
        listLabel = []

        for elem in db.topTenSongsByUser():
            res = elem[3]
            data[res] = data[res] + 1.

        for i in label:
            for elem in data:
                if i == elem and data[elem] != 0.:
                    listData.append(data[elem])
                    listLabel.append(elem)
                    
        ax.pie(listData,labels=listLabel, autopct='%1i%%',shadow=True)
        ax.set_title("Genre Distribution within Top 10 Songs by User Average")

        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)

    def drawFigure(self, canvas, figureFunc, db):
        figure_canvas_agg = FigureCanvasTkAgg(figureFunc(db), canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)

