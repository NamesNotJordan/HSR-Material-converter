import math


PURPLE_EXP = 20000
BLUE_EXP = 5000
GREEN_EXP = 1000

# Books
# Converts number of blue and greenbooks into equivalent number of purple books
def upscaleBooks(blueBooks =0, greenBooks=0):
    blue = blueBooks*BLUE_EXP
    green = greenBooks*GREEN_EXP
    return math.floor((blue+green)/PURPLE_EXP)


# returns number of 
def findRequiredBooks(target):
    targetExp = target * PURPLE_EXP
    blueRequired = math.floor(targetExp/BLUE_EXP)
    greenRequired = math.ceil((targetExp%BLUE_EXP)/GREEN_EXP)
    return (blueRequired, greenRequired)


# Traces
def upscaleTrace(blueMat, greenMat):
    pass