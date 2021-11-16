# Art Attack

## Brief Overview of Folder Structure
Here is a brief description of all the folers in the repo and what they're used for!
- `arduino-src`: where all the arduino code files live.
- `python-src`: where all the python package files live.
- `scripts`: home to any python scripts that are external to the package.

## Setting up the Python environment
In order to run the code you need to have a working version of Python 3.6 (or greater) installed on your computer. A list of required dependencies can be found in the `requirements.txt` file. You'll also need to install the latest version of OpenCV.  

If you are running Ubuntu (or something similar), try running the following lines of code to automatically setup a python virtual environment with everything you'll need.
```
sudo apt update
sudo apt install python3-opencv
source setup-python-venv.sh
```
