# LD_imageProcessing.py

# Brianna Drew
# March 7, 2021
# ID: #0622446
# Lab #6, Part #3

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

        # set new RGB values of current pixel
        myImage[x][y][0] = average
        myImage[x][y][1] = average
        myImage[x][y][2] = average

# detect edges within image and convert to black if edge detected, white if not
for x in range(0, height-2):
    for y in range(0,width-2):
        this = myImage[x][y][0] # colour of current pixel
        right = myImage[x+1][y][0] # colour of pixel to the right
        below = myImage[x][y+1][0] # colour of pixel below
        diff_right = abs(this - right) # difference in colour between current and right pixel
        diff_below = abs(this - below) # difference in colour between current and below pixel

        if diff_right > 0.0013 and diff_below > 0.0013:
            # set to black
            myImage[x][y][0] = 0
            myImage[x][y][1] = 0
            myImage[x][y][2] = 0
        else:
            # set to white
            myImage[x][y][0] = 1
            myImage[x][y][1] = 1
            myImage[x][y][2] = 1
            
# show resulting image        
imgplot = matplotlib.pyplot.imshow(myImage)
matplotlib.pyplot.show()
