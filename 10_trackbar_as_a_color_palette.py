import cv2 as cv
import numpy as np

# Here we will create a simple application which shows the color you specify. 
# You have a window which shows the color and three trackbars to specify each of B,G,R colors.
# You slide the trackbar and correspondingly window color changes. By default, initial color will be set to Black.

# For cv.getTrackbarPos() function, 
# first argument:  is the trackbar name, 
# second argument: is the window name to which it is attached, 
# third argument:  is the default value, 
# fourth argument: is the maximum value,
# fifth argument:  is the callback function which is executed everytime trackbar value changes. 

# The callback function always has a default argument which is the trackbar position. 
# In our case, function does nothing, so we simply pass.

# Another important application of trackbar is to use it as a button or switch. 
# OpenCV, by default, doesn’t have button functionality. So you can use trackbar to get such functionality.
# In our application, we have created one switch in which application works only if switch is ON, otherwise screen is always black.

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

# create trackbars for color change
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27: # esc button
        break

    # get current positions of four trackbars
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    s = cv.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv.destroyAllWindows()