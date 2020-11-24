import PySimpleGUI as sg


# sg.theme_previewer()


# sg.theme('Dark Grey 9')  # set window theme

# guiThemes = [[sg.theme_previewer()]]

# window = sg.Window('H.A.M.L.', guiThemes, font=(
#         "Roboto", 12), size=(1920, 1080), finalize=True)

# while True:
#     event, values = window.read()

#     # End progam when window is closed
#     if event == sg.WINDOW_CLOSED:
#         break


# # close the program
# window.close()


# s = 'smitty\'s house'
# print(s)
# s = re.sub('(?<=[a-z])\'(?=[a-z])', '', s)
# print(s)

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

# layout = [  [sg.Text('Click on field')],
#             [sg.Input(key='_INPUT1_')],
#             [sg.Input(key='_INPUT2_')],
#             [sg.T('', size=(40,1), key='_TEXT_')],
#             [sg.Button('Read')]]

# window = sg.Window('Demonstration of focus', layout)

# current_focus = None
# while True:             # Event Loop
#     event, values = window.Read(timeout=500)
#     if event is None:
#         break
#     element = window.FindElementWithFocus()
#     if element is not None and element != current_focus:
#         window.Element('_TEXT_').Update(f'Focus changed....Element with focus = {element.Key}')
#         current_focus = element
#         if element.Key == '_INPUT2_':
#             sg.Popup('You clicked in the input field',
#                      'that will open your newly designed date chooser window(s)')


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


# Main program


# while True:
#     m_Fld1_txt = ''
#     m_Fld2_txt = ''
#     m_Fld3_txt = ''

#     layout = [[sg.Text('Text Field1:'),
#                sg.Input(default_text=m_Fld1_txt,
#                         size=(10, 1),
#                         key='Fld1')],
#               [sg.Text('Text Field2:'),
#                sg.Input(default_text=m_Fld2_txt,
#                         size=(10, 1),
#                         key='Fld2')],
#               [sg.Text('Text Field3:'),
#                sg.Input(default_text=m_Fld3_txt,
#                         size=(10, 1),
#                         key='Fld3')],
#               [sg.Text("Date Established"), sg.Input(key='-dateEstablished-C01-', size=(20, 1)),
#                sg.CalendarButton('Date Picker', close_when_date_chosen=True, format='%Y-%m-%d', target='-dateEstablished-C01-', no_titlebar=True, key='Calendar-C01')],
#               [sg.Text('Press F01 to Proceed, Esc to Exit.')],
#               [sg.Button('ESC'),
#                sg.Button('F01')]]

#     window = sg.Window('Test Form',
#                        layout,
#                        size=(800, 360),
#                        disable_close=True,
#                        font='fixedsys',
#                        finalize=True)

#     window.TKroot.focus_force()         # Force this window to have focus

# #   window.Element('Fld1').SetFocus()
# #   window.Element('Fld2').SetFocus()
#     window.Element('Fld3').SetFocus()   # Force this field to have focus

#     m_Event, m_Values = window.Read()
#     window.Close()

#     if m_Event == 'ESC':
#         break
#     else:
#         pass

#     m_Fld1_txt = m_Values['Fld1']
#     m_Fld2_txt = m_Values['Fld2']
#     m_Fld3_txt = m_Values['Fld3']

#  Code to process m_Fld1_txt, m_Fld2_txt, m_Fld3_txt goes here.

#  Ultimately, go around 'while' loop again, until 'ESC' button clicked.


"""
    A simple "settings" implementation.  Load/Edit/Save settings for your programs
    Uses json file format which makes it trivial to integrate into a Python program.  If you can
    put your data into a dictionary, you can save it as a settings file.

    Note that it attempts to use a lookup dictionary to convert from the settings file to keys used in 
    your settings window.  Some element's "update" methods may not work correctly for some elements.

    Copyright 2020 PySimpleGUI.com
    Licensed under LGPL-3
"""

##################### Make a settings window #####################


def create_settings_window():
    # sg.theme(values['-THEME-'][0])

    def TextLabel(text): return sg.Text(text + ':', justification='r', size=(15, 1))

    theme_layout = [[sg.Text('Settings', font='Any 15')],
              [TextLabel('Theme'), sg.Combo(sg.theme_list(), size=(20, 20), key='-THEME-')],
              [sg.Button('Save'), sg.Button('Exit')]]

    window = sg.Window('Settings', theme_layout, keep_on_top=True, finalize=True)

    return window

##################### Main Program Window & Event Loop #####################


def create_main_window():
    # sg.theme(values['-THEME-'][0])

    layout = [[sg.T('This is my main application')],
              [sg.T('Add your primary window stuff in here')],
              [sg.B('Ok'), sg.B('Exit'), sg.B('Change Settings')]]

    return sg.Window('Main Application', layout)


def main():
    window = None
    sg.theme('Dark Grey 9')
    while True:             # Event Loop
        if window is None:
            window = create_main_window()

        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Change Settings':
            event, values = create_settings_window().read(close=True)
            if event == 'Save':
                window.close()
                window = None

        try:
            print(values['-THEME-'])
            sg.theme(values['-THEME-'])
        except:
            print('err')
    window.close()


main()
