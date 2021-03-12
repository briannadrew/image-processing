# GS_imageProcessing.py

# Brianna Drew
# March 7, 2021
# ID: #0622446
# Lab #6, Part #1

# import required libraries
import matplotlib.pyplot
import numpy

myImage = matplotlib.pyplot.imread('flower.png') # import png image

# get height and width of image
height = myImage.shape[0]
width = myImage.shape[1]

# convert image to grayscale, pixel by pixel
for x in range(0, height-1):
    for y in range(0,width-1):
        average = (myImage[x][y][0] + myImage[x][y][1] + myImage[x][y][2]) / 3 # get average of RGB values for current pixel

        # set new RGB values of current pixels
        myImage[x][y][0] = average
        myImage[x][y][1] = average
        myImage[x][y][2] = average

# show resulting image
imgplot = matplotlib.pyplot.imshow(myImage)
matplotlib.pyplot.show()
