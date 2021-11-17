import cv2 as cv

# import sys module for computer system operation
import sys

# add samples and data folder path to open cv package
# the folder path is relative to the current directory or folder where the code is located. 
cv.samples.addSamplesDataSearchPath("..\\samples\\data")

# get sample file path for "starry_night.jpg"
filePath = cv.samples.findFile("starry_night.jpg")


img = cv.imread(filePath)


if img is None:
    sys.exit("Could not read the image.")


cv.imshow("Display window", img)

# pause execution here by waiting for a user to press a key
k = cv.waitKey(0)

# if user typed s save file as PNG file
if k == ord("s"):
    cv.imwrite("starry_night.png", img)

cv.destroyAllWindows()