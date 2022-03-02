#-- IMPORTS --

import csv
import math
import os
import random
import sys
import time
from datetime import date, datetime

from cairosvg import svg2png  # CairoSvg - converts `.svg` to `.png`
from PIL.PngImagePlugin import PngImageFile, PngInfo # Gives `png` files metadata
from simple_chalk import (black, blue, green, red,  # Colours terminal text
                          yellow)

#-- GLOBALS --


#-- CONSTANTS --


#-- FUNCTIONS --

    # GENERATES RANDOM COLOUR
def colourGen(darkerTrue=None):

    colour = ""
    r = random.randint(55,200)
    g = random.randint(55,200)
    b = random.randint(55,200)
    if darkerTrue == None:
        colour = f"rgb({r},{g},{b})"

    if darkerTrue:
        r = r * 0.25
        g = g * 0.25
        b = b * 0.25
        colour = f"rgb({r},{g},{b})"

    return colour

    # Creates element with 
def createElem(path,name,colour=None,strokeColour="Black",strokeWeight=LINE_WEIGHT,DarkerTrue=None,text="",fillColour=None):
    
    if colour != None:
        elementColour = colour
    else:
        elementColour=colourGen(DarkerTrue)
    if text != "":
        end = f">{text}</path>"
    else:
        end = "/>"
    element = f"""<!-- {name} -->
        <path d="{path}"
        fill="{elementColour}" stroke="{strokeColour}" stroke-width="{strokeColour}" {end}"""
    return element

###################################################

#-- MAIN CODE --

while run:
    print("Inputs marked with"+ )
    seriesName = input("Series Name *\n ")
    while newPath != True:
        name = input("Name *\n> ")
        path = input("Path *\n> ")
        colour = input("Colour\n> ")
        createElem(path, name)
