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

            [[sg.Text("Top 10 Songs by Average Rating")],
             [sg.Table(values=self.db.topTenSongsByAverage(), headings=['Song Title', 'Album Title', 'Genre', 'Duration', 'Link',
                                                               'Release Year', 'Average Rating', 'Number of Listeners', 'Rating'], key='-TABLE-I01-', enable_events=True, size=(1220, 15))],
            [sg.Text("Top 10 Songs by User Rating")],
             [sg.Table(values=self.db.topTenSongsByUser(), headings=['Song Title', 'Album Title', 'Genre', 'Duration', 'Link',
                                                               'Release Year', 'Average Rating', 'Number of Listeners', 'Rating'], key='-TABLE-I02-', enable_events=True, size=(1220, 15))]
             ],
            key='I01'
        )  # end of tab Record Label

        ### #### #### #### #### #### #### #### #### ###
        #          END OF CREATE TABLE TABS           #
        ### #### #### #### #### #### #### #### #### ###

        # to be replaced by a nested tab group
        insightsTab = sg.Tab(
            'Insights',
            [[sg.TabGroup(
                [[
                    top10Songs
                ]],
                key='tabgroupInsights',
                enable_events=True
            )  # end of TabGroup
            ]],

            key='insights_tab'

        )  # end of tab insights

        return insightsTab
