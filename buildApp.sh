#!/bin/bash

./rm_exe.sh
pyinstaller --windowed ./gui.py
python TCLChanger.py
