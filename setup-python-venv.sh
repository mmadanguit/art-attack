#!/usr/bin/env bash

VENV="art-attack"
FOLDER="$PWD/.venv/$VENV"
echo "#####Setup Python Environment#####"
echo "Searching for $VENV python virtual environment..."
if [ -d "$FOLDER" ]; then
    echo "Found $FOLDER. Attempting to activate..."
    source $FOLDER/bin/activate
    echo "Virtual environment activated."
else
    echo "Virtual environment not found! Attempting to create a new one..."
    [ ! -d "$PWD/.venv" ] && mkdir "$PWD/.venv"
    python3 -m venv $FOLDER
    source $FOLDER/bin/activate
    echo "Virtual environment activated."
fi
echo "Installing requirements..."
pip install --upgrade pip
python -m pip install -r requirements.txt
echo "Installing symlinks to packages in python-src..."
pip install -e $PWD
echo "#####DONE#####"

