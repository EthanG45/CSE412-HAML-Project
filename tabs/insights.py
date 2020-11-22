import PySimpleGUI as sg

### #### #### #### #### #### #### #### #### ###
#            INSIGHTS TABLE TABS              #
### #### #### #### #### #### #### #### #### ###


class InsightsTab:
    def __init__(self, db):
        self.db = db

    def insightsTabGUI(self):
        top10Songs = sg.Tab(
            'Top 10 Songs',

            # TODO table sizing is weird
            [[sg.Text("Top 10 Songs by Average Rating")],
             [sg.Table(values=self.db.topTenSongsByAverage(), headings=['Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                                                                        'Release Year', 'Average Rating', 'Number of Listeners', 'Rating'], key='-AVG-TABLE-I01-', enable_events=True, size=(1220, 10))],
             [sg.Text("Top 10 Songs by User Rating")],
             [sg.Table(values=self.db.topTenSongsByUser(), headings=['Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                                                                     'Release Year', 'Average Rating', 'Number of Listeners', 'Rating'], key='-USER-TABLE-I01-', enable_events=True, size=(1220, 10))]
             ],
            key='I01'
        )  # end of tab Record Label
        
        top10Albums = sg.Tab(
            'Top 10 Albums',
            # TODO table sizing is weird
            [[sg.Text("Top 10 Albums by Average Rating")],
             [sg.Table(values=self.db.topTenAlbumsByAverage(), headings=['Title', 'Album Duration',
                                                                   'Cover Art URL', 'Averaqe Rating', 'Number of Listeners', 'User Rating'], key='-AVG-TABLE-I02-', enable_events=True, size=(1220, 10))],
             [sg.Text("Top 10 Albums by User Rating")],
             [sg.Table(values=self.db.topTenAlbumsByUser(), headings=['Title', 'Album Duration',
                                                                   'Cover Art URL', 'Averaqe Rating', 'Number of Listeners', 'User Rating'], key='-USR-TABLE-I02-', enable_events=True, size=(1220, 10))]
             ],
            key='I02'
        )  # end of tab Record Label
        
        top10WorstSongs = sg.Tab(
            'Top 10 Worst Songs',

            # TODO table sizing is weird
            [[sg.Text("Top 10 Worst Songs by Average Rating")],
             [sg.Table(values=self.db.topTenSongsByAverageWorst(), headings=['Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                                                                        'Release Year', 'Average Rating', 'Number of Listeners', 'Rating'], key='-AVG-TABLE-I03-', enable_events=True, size=(1220, 10))],
             [sg.Text("Top 10 Worst Songs by User Rating")],
             [sg.Table(values=self.db.topTenSongsByUserWorst(), headings=['Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                                                                     'Release Year', 'Average Rating', 'Number of Listeners', 'Rating'], key='-USER-TABLE-I03-', enable_events=True, size=(1220, 10))]
             ],
            key='I03'
        )  # end of tab Record Label

        top10WorstAlbums = sg.Tab(
            'Top 10 Worst Albums',
            # TODO table sizing is weird
            [[sg.Text("Top 10 Worst Albums by Average Rating")],
             [sg.Table(values=self.db.topTenAlbumsByAverageWorst(), headings=['Title', 'Album Duration',
                                                                   'Cover Art URL', 'Averaqe Rating', 'Number of Listeners', 'User Rating'], key='-AVG-TABLE-I04-', enable_events=True, size=(1220, 10))],
             [sg.Text("Top 10 Worst Albums by User Rating")],
             [sg.Table(values=self.db.topTenAlbumsByUserWorst(), headings=['Title', 'Album Duration',
                                                                   'Cover Art URL', 'Averaqe Rating', 'Number of Listeners', 'User Rating'], key='-USR-TABLE-I04-', enable_events=True, size=(1220, 10))]
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
