import PySimpleGUI as sg
import re
import sql
import time
from faker import Faker
fake = Faker()


db = sql.Database()

# print(int(round(time.time())))

# print(db.sqlReadAny("SELECT A.artistName FROM Artist A, Contains C, Song S, Played P, Musician M WHERE S.title = 'not that' AND S.songId = C.songId AND C.albumId = P.albumId AND P.musicianId = M.musicianId AND M.artistId = A.artistId"))
# print(db.findRecordLabelBySongName('hundred school'))
# print(db.sqlReadAny("SELECT R.companyName FROM musician M, played P1, publishes P2, recordLabel R WHERE M.musicianId = P1.musicianId AND P1.albumId = P2.albumId AND P2.recordLabelId = R.recordLabelId AND M.instrument = 'Drums'"))
# print(db.findcompanyNameByBandName('SlateBlue character'))
# print(db.findListOfCompanyNameByInstrument('Drums'))
# print(db.searchArtist('Darlene Lewis'))
# print(db.searchMusician('SlateBlue character'))
# db.insertRecordLabel('Oreo', '2020-11-20',"Texas's house")
# print(db.sqlReadAny("SELECT * FROM recordLabel WHERE companyName = 'Oreo';"))
# print(db.deleteRecordLabel('Arvin'))

# s = 'smitty\'s house'
# print(s)
# s = re.sub('(?<=[a-z])\'(?=[a-z])', '', s)
# print(s)

# #!/usr/bin/env python
# import PySimpleGUI as sg

# """
#     Simple test harness to demonstate how to use the CalendarButton and the get date popup
# """
# # sg.theme('Dark Red')
# layout = [[sg.Text('Date Chooser Test Harness', key='-TXT-')],
#       [sg.Input(key='-IN-', size=(20,1)), sg.CalendarButton('Cal US No Buttons Location (0,0)', close_when_date_chosen=True,  target='-IN-', location=(0,0), no_titlebar=False, )],
#       [sg.Input(key='-IN3-', size=(20,1)), sg.CalendarButton('Cal Monday', title='Pick a date any date', no_titlebar=True, close_when_date_chosen=False,  target='-IN3-', begin_at_sunday_plus=1, month_names=('студзень', 'люты', 'сакавік', 'красавік', 'май', 'чэрвень', 'ліпень', 'жнівень', 'верасень', 'кастрычнік', 'лістапад', 'снежань'), day_abbreviations=('Дш', 'Шш', 'Шр', 'Бш', 'Жм', 'Иш', 'Жш'))],
#       [sg.Input(key='-IN2-', size=(20,1)), sg.CalendarButton('Cal German Feb 2020',  target='-IN2-',  default_date_m_d_y=(2,None,2020), locale='de_DE', begin_at_sunday_plus=1 )],
#       [sg.Input(key='-IN4-', size=(20,1)), sg.CalendarButton('Cal Format %m-%d Jan 2020',  target='-IN4-', format='%m-%d', default_date_m_d_y=(1,None,2020), )],
#       [sg.Button('Read'), sg.Button('Date Popup'), sg.Exit()]]

# window = sg.Window('window', layout)

# while True:
#     event, values = window.read()
#     print(event, values)
#     if event in (sg.WIN_CLOSED, 'Exit'):
#         break
#     elif event == 'Date Popup':
#         sg.popup('You chose:', sg.popup_get_date())
# window.close()

# import PySimpleGUI as sg

layout = [  [sg.Text('Click on field')],
            [sg.Input(key='_INPUT1_')],
            [sg.Input(key='_INPUT2_')],
            [sg.T('', size=(40,1), key='_TEXT_')],
            [sg.Button('Read')]]

window = sg.Window('Demonstration of focus', layout)

current_focus = None
while True:             # Event Loop
    event, values = window.Read(timeout=500)
    if event is None:
        break
    element = window.FindElementWithFocus()
    if element is not None and element != current_focus:
        window.Element('_TEXT_').Update(f'Focus changed....Element with focus = {element.Key}')
        current_focus = element
        if element.Key == '_INPUT2_':
            sg.Popup('You clicked in the input field',
                     'that will open your newly designed date chooser window(s)')


# layout = [[sg.Text('Enter Value:')],
#           [sg.Input(do_not_clear=False), sg.T('Not Selected ', size=(
#               52, 1), justification='left', text_color='red', background_color='white', key='_USERNAME_')],
#           [sg.Button('Enter'), sg.Exit()],
#           [sg.Text('List Of Values:')],
#           [sg.Listbox(values=('value1', 'value2', 'value3'), size=(30, 2), key='_LISTBOX_')]]

# window = sg.Window('My Application', layout)

# while True:
#     event, values = window.Read()
#     print(event, values)
#     if event is None or event == 'Exit':
#         break
#     if event == 'Enter':
#         window.Element('_LISTBOX_').Update(
#             values=[event, values, 'new value 3'])
#         window.FindElement('_USERNAME_').Update(values[0])
# window.Close()

# QT_ENTER_KEY1 = 'special 16777220'
# QT_ENTER_KEY2 = 'special 16777221'

# layout = [[sg.T('Test of Enter Key use')],
#           [sg.In(key='_IN_')],
#           [sg.Button('Button 1', key='_1_')],
#           [sg.Button('Button 2', key='_2_')],
#           [sg.Button('Button 3', key='_3_')], ]

# window = sg.Window('My new window', layout,
#                     return_keyboard_events=True)
#  while True:             # Event Loop
#     event, values = window.Read()
#     if event is None:
#         break
#     if event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):         # Check for ENTER key
#         # go find element with Focus
#         elem = window.FindElementWithFocus()
#         if elem is not None and elem.Type == sg.ELEM_TYPE_BUTTON:       # if it's a button element, click it
#             elem.Click()
#         # check for buttons that have been clicked
#     elif event == '_1_':
#         print('Button 1 clicked')
#     elif event == '_2_':
#         print('Button 2 clicked')
#     elif event == '_3_':
#         print('Button 3 clicked')
