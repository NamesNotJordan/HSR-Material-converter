import math


PURPLE_EXP = 20000
BLUE_EXP = 5000
GREEN_EXP = 1000
class Converter():
    # Converts number of blue and greenbooks into equivalent number of purple books
    @staticmethod
    def upscaleBooks(blueBooks, greenBooks):
        blue = blueBooks*BLUE_EXP
        green = greenBooks*GREEN_EXP
        return math.floor((blue+green)/PURPLE_EXP)
    
    
    # returns number of 
    @staticmethod
    def findRequiredBooks(target):
        targetExp = target * PURPLE_EXP
        blueRequired = math.floor(targetExp/BLUE_EXP)
        greenRequired = math.ceil((targetExp%BLUE_EXP)/GREEN_EXP)
        return (blueRequired, greenRequired)
    
    @staticmethod
    def upscaleTrace(blueMat, greenMat):
        pass
