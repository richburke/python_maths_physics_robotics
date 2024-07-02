import os
import sys

sys.path.extend([os.getcwd()])

def inches_to_centimeters(inches):
    return inches * 2.54

def centimeters_to_inches(centimeters):
    return centimeters / 2.54

def feet_to_miles(feet):
    return feet / 5280
