import PySimpleGUI as sg

### #### #### #### #### #### #### #### #### ###
#            INSIGHTS TABLE TABS              #
### #### #### #### #### #### #### #### #### ###


class InsightsTab:
    def __init__(self, db):
        self.db = db
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
            [[sg.Text("Top 10 Songs by Average Rating")],
             [sg.Table(values=self.top10SongByAverage, headings=['Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                                                                 'Release Year', 'Average Rating', 'Listeners', 'Rating'], key='-AVG-TABLE-I01-', enable_events=True, size=(1220, 10))],
             [sg.Text("Top 10 Songs by User Rating")],
             [sg.Table(values=self.top10SongByUser, headings=['Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                                                              'Release Year', 'Average Rating', 'Listeners', 'Rating'], key='-USER-TABLE-I01-', enable_events=True, size=(1220, 10))]
             ],
            key='I01'
        )  # end of tab Record Label

        top10Albums = sg.Tab(
            'Top 10 Albums',
            # TODO table sizing is weird
            [[sg.Text("Top 10 Albums by Average Rating")],
             [sg.Table(values=self.top10AlbumByAverage, headings=['Title', 'Album Duration',
                                                                  'Cover Art URL', 'Averaqe Rating', 'Listeners', 'User Rating'], key='-AVG-TABLE-I02-', enable_events=True, size=(1220, 10))],
             [sg.Text("Top 10 Albums by User Rating")],
             [sg.Table(values=self.top10AlbumByUser, headings=['Title', 'Album Duration',
                                                               'Cover Art URL', 'Averaqe Rating', 'Listeners', 'User Rating'], key='-USER-TABLE-I02-', enable_events=True, size=(1220, 10))]
             ],
            key='I02'
        )  # end of tab Record Label

        top10WorstSongs = sg.Tab(
            'Top 10 Worst Songs',

            # TODO table sizing is weird
            [[sg.Text("Top 10 Worst Songs by Average Rating")],
             [sg.Table(values=self.top10WorstSongByAverage, headings=['Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                                                                      'Release Year', 'Average Rating', 'Listeners', 'Rating'], key='-AVG-TABLE-I03-', enable_events=True, size=(1220, 10))],
             [sg.Text("Top 10 Worst Songs by User Rating")],
             [sg.Table(values=self.top10WorstSongByUser, headings=['Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                                                                   'Release Year', 'Average Rating', 'Listeners', 'Rating'], key='-USER-TABLE-I03-', enable_events=True, size=(1220, 10))]
             ],
            key='I03'
        )  # end of tab Record Label

        top10WorstAlbums = sg.Tab(
            'Top 10 Worst Albums',
            # TODO table sizing is weird
            [[sg.Text("Top 10 Worst Albums by Average Rating")],
             [sg.Table(values=self.top10WorstAlbumByAverage, headings=['Title', 'Album Duration',
                                                                       'Cover Art URL', 'Averaqe Rating', 'Listeners', 'User Rating'], key='-AVG-TABLE-I04-', enable_events=True, size=(1220, 10))],
             [sg.Text("Top 10 Worst Albums by User Rating")],
             [sg.Table(values=self.top10WorstAlbumByUser, headings=['Title', 'Album Duration',
                                                                    'Cover Art URL', 'Averaqe Rating', 'Listeners', 'User Rating'], key='-USER-TABLE-I04-', enable_events=True, size=(1220, 10))]
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
