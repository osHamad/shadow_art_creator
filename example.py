import cv2 as cv
import numpy as np

im = cv.imread('frames/frame_.png')
im = cv.cvtColor(im, cv.COLOR_RGB2GRAY)
cv.Canny(im, 100, 200)
cv.imshow('flooded image with invert', im)
cv.waitKey(0)

th, im_th = cv.threshold(im, 100, 200, cv.THRESH_BINARY_INV)

# Floodfill arena area with value 128, i.e. mid-grey
floodval = 128
cv.floodFill(im_th, None, (0, 0), floodval)

# Extract filled area alone
arena = ((im_th==floodval) * 255).astype(np.uint8)

cv.imshow('flooded image with invert', arena)
cv.waitKey(0)

