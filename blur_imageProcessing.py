# blur_imageProcessing.py

# Brianna Drew
# March 7, 2021
# ID: #0622446
# Lab #6, Part #2

# import required libraries
import matplotlib.pyplot
import numpy

myImage = matplotlib.pyplot.imread('flower.png') # import png image

# get height and width of image
height = myImage.shape[0]
width = myImage.shape[1]

# gaussian blur for a radius of 3 pixels (average of current pixel + 48 surrounding neighbours)
for x in range(3, height-4):
    for y in range(3,width-4):
        # red values
        average_R = (myImage[x][y][0] + myImage[x+1][y][0] + myImage[x-1][y][0] +
        myImage[x][y+1][0] + myImage[x][y-1][0] + myImage[x-1][y-1][0] +
        myImage[x+1][y-1][0] + myImage[x-1][y+1][0] + myImage[x+1][y+1][0] +
        myImage[x+2][y][0] + myImage[x-2][y][0] + myImage[x][y+2][0] +
        myImage[x][y-2][0] + myImage[x-2][y-2][0] + myImage[x+2][y-2][0] +
        myImage[x-2][y+2][0] + myImage[x+2][y+2][0] + myImage[x-1][y-2][0] +
        myImage[x-2][y-1][0] + myImage[x+1][y-2][0] + myImage[x+2][y-1][0] +
        myImage[x-1][y+2][0] + myImage[x-2][y+1][0] + myImage[x+1][y+2][0] +
        myImage[x+2][y+1][0] + myImage[x-3][y-3][0] + myImage[x+3][y-3][0] +
        myImage[x-3][y+3][0] + myImage[x+3][y+3][0] + myImage[x-3][y-2][0] +
        myImage[x-3][y-1][0] + myImage[x-3][y][0] + myImage[x-3][y+1][0] +
        myImage[x-3][y+2][0] + myImage[x-2][y+3][0] + myImage[x-1][y+3][0] +
        myImage[x][y+3][0] + myImage[x+1][y+3][0] + myImage[x+2][y+3][0] +
        myImage[x+3][y+2][0] + myImage[x+3][y+1][0] + myImage[x+3][y][0] +
        myImage[x+3][y-1][0] + myImage[x+3][y-2][0] + myImage[x+2][y-3][0] +
        myImage[x+1][y-3][0] + myImage[x][y-3][0] + myImage[x-1][y-3][0] +
        myImage[x-2][y-3][0]) / 49

        # green values
        average_G = (myImage[x][y][1] + myImage[x+1][y][1] + myImage[x-1][y][1] +
        myImage[x][y+1][1] + myImage[x][y-1][1] + myImage[x-1][y-1][1] +
        myImage[x+1][y-1][1] + myImage[x-1][y+1][1] + myImage[x+1][y+1][1] +
        myImage[x+2][y][1] + myImage[x-2][y][1] + myImage[x][y+2][1] +
        myImage[x][y-2][1] + myImage[x-2][y-2][1] + myImage[x+2][y-2][1] +
        myImage[x-2][y+2][1] + myImage[x+2][y+2][1] + myImage[x-1][y-2][1] +
        myImage[x-2][y-1][1] + myImage[x+1][y-2][1] + myImage[x+2][y-1][1] +
        myImage[x-1][y+2][1] + myImage[x-2][y+1][1] + myImage[x+1][y+2][1] +
        myImage[x+2][y+1][1] + myImage[x-3][y-3][1] + myImage[x+3][y-3][1] +
        myImage[x-3][y+3][1] + myImage[x+3][y+3][1] + myImage[x-3][y-2][1] +
        myImage[x-3][y-1][1] + myImage[x-3][y][1] + myImage[x-3][y+1][1] +
        myImage[x-3][y+2][1] + myImage[x-2][y+3][1] + myImage[x-1][y+3][1] +
        myImage[x][y+3][1] + myImage[x+1][y+3][1] + myImage[x+2][y+3][1] +
        myImage[x+3][y+2][1] + myImage[x+3][y+1][1] + myImage[x+3][y][1] +
        myImage[x+3][y-1][1] + myImage[x+3][y-2][1] + myImage[x+2][y-3][1] +
        myImage[x+1][y-3][1] + myImage[x][y-3][1] + myImage[x-1][y-3][1] +
        myImage[x-2][y-3][1]) / 49

        # blue values
        average_B = (myImage[x][y][2] + myImage[x+1][y][2] + myImage[x-1][y][2] +
        myImage[x][y+1][2] + myImage[x][y-1][2] + myImage[x-1][y-1][2] +
        myImage[x+1][y-1][2] + myImage[x-1][y+1][2] + myImage[x+1][y+1][2] +
        myImage[x+2][y][2] + myImage[x-2][y][2] + myImage[x][y+2][2] +
        myImage[x][y-2][2] + myImage[x-2][y-2][2] + myImage[x+2][y-2][2] +
        myImage[x-2][y+2][2] + myImage[x+2][y+2][2] + myImage[x-1][y-2][2] +
        myImage[x-2][y-1][2] + myImage[x+1][y-2][2] + myImage[x+2][y-1][2] +
        myImage[x-1][y+2][2] + myImage[x-2][y+1][2] + myImage[x+1][y+2][2] +
        myImage[x+2][y+1][2] + myImage[x-3][y-3][2] + myImage[x+3][y-3][2] +
        myImage[x-3][y+3][2] + myImage[x+3][y+3][2] + myImage[x-3][y-2][2] +
        myImage[x-3][y-1][2] + myImage[x-3][y][2] + myImage[x-3][y+1][2] +
        myImage[x-3][y+2][2] + myImage[x-2][y+3][2] + myImage[x-1][y+3][2] +
        myImage[x][y+3][2] + myImage[x+1][y+3][2] + myImage[x+2][y+3][2] +
        myImage[x+3][y+2][2] + myImage[x+3][y+1][2] + myImage[x+3][y][2] +
        myImage[x+3][y-1][2] + myImage[x+3][y-2][2] + myImage[x+2][y-3][2] +
        myImage[x+1][y-3][2] + myImage[x][y-3][2] + myImage[x-1][y-3][2] +
        myImage[x-2][y-3][2]) / 49

        # set new RGB values of current pixel
        myImage[x][y][0] = average_R
        myImage[x][y][1] = average_G
        myImage[x][y][2] = average_B

# show resulting image
imgplot = matplotlib.pyplot.imshow(myImage)
matplotlib.pyplot.show()
