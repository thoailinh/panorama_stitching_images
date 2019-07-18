# panorama stitching images

Matching and stitching images related to a complete image(panorama).

## Getting Started

### Prerequisites

When I work my project, i am using ubuntu 18.04.2.

You need to install the libraries to run project.

```
Python3.6 
Opencv3.4.2 contrib
Numpy
PyQT5
```

### Installing

I use vs code and install pip before install libraries.

```
pip install --user pyqt5  
sudo apt-get install python3-pyqt5  
sudo apt-get install pyqt5-dev-tools
sudo apt-get install qttools5-dev-tools
pip install numpy
pip install opencv-contrib-python
```

## Running

Run file main.py

```
python3 main.py
```
Show application panorama have 3 buttons(NOTE, OPEN WITH FILES, PANORAMA).

Click button "NOTE" to see message before using.

Click button "OPEN WITH FILES" and choose all file input images.

Click button "PANORAMA" and wait some seconds to show window to save file result.

To compute result images fast or low depent on resolution of input images.

### Input

Names of input images have rename order from left to right and put all to one folder.

```
/1.jpg
/2.jpg
/3.jpg
```

### Out put

Result file

church.jpg

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

