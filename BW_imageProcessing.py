# BW_imageProcessing.py

# Brianna Drew
# March 7, 2021
# ID: #0622446
# Lab #6, Part #1

# IMPORT REQUIRED LIBRARIES
import matplotlib.pyplot
import numpy

myImage = matplotlib.pyplot.imread('flower.png') # IMPORT PNG IMAGE

# GET HEIGHT AND WIDTH OF IMAGE
height = myImage.shape[0]
width = myImage.shape[1]

# CONVERT IMAGE TO BLACK AND WHITE, PIXEL BY PIXEL 
for x in range(0, height-1):
    for y in range(0,width-1):
        average = (myImage[x][y][0] + myImage[x][y][1] + myImage[x][y][2]) / 3 # GET AVERAGE OF RGB VALUES FOR CURRENT PIXEL
        # SET COLOUR OF PIXEL TO WHATEVER IT'S CLOSEST TO
        if average < 0.5:
            colour = 0 # SET TO BLACK
        else:
            colour = 1 # SET TO WHITE

        # SET NEW RGB VALUES OF CURRENT PIXELS
        myImage[x][y][0] = colour
        myImage[x][y][1] = colour
        myImage[x][y][2] = colour

# SHOW RESULTING IMAGE
imgplot = matplotlib.pyplot.imshow(myImage)
matplotlib.pyplot.show()
