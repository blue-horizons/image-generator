import random
import math
from cairosvg import svg2png
import os

if os.path.isdir("HAWSIES"):
    os.chdir("HAWSIES")
else:
    os.mkdir("HAWSIES")
    os.chdir("HAWSIES")
count = 0

#svgTemplate = open("hawsie-template.svg","r")

while count <= 999:
    formatNum =  '{:03}'.format(count)
    filename = f"hawsie #{formatNum}.png"
    print(filename)


    svgOut = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg height="86" width="86">
"""

    #generate random colour

    def colourGen(darkerTrue):
    
        r = random.randint(55,200)
        g = random.randint(55,200)
        b = random.randint(55,200)
        if darkerTrue:
            r = r * 0.25
            g = g * 0.25
            b = b * 0.25
    
        colour = f"rgb({r},{g},{b})"
    
        return colour

    #-- Background --

    background = colourGen(None)
    print("background colour is " + background)

    #-- Face --

    furColour = colourGen(None)

    face = f"""
    <!-- Face -->
    <path d="M 19 19 L 23 8 L 27 19 L 31 8 L 35 19 L 63 19 C 65 19 67 21 67 23 L 67 43 L 43 43 C 42 43 41 44 41 45 L 41 57 C 41 58 42 59 43 59 L 67 59 C 67 61 65 63 63 63 L 23 63 C 21 63 19 61 19 59 Z" 
    fill="{furColour}" stroke="black" stroke-width="0.5" />"""
    
    svgOut = svgOut + face


    #-- Body --

    body = f"""
    <!-- Body -->
    <path d="M 19 55 L -1 55 L -1 87 L 27 87 L 27 63 L 23 63 C 21 63 19 61 19 59 Z" 
    fill="#{furColour}" stroke="black" stroke-width="0.5" />"""

    svgOut = svgOut + body

    #-- Face Spots --

    randomiser = random.randint(0, 99)
    spotFill = colourGen(True)
    if randomiser % 2 == 0:
        spots = f"""
        <!-- Spots -->
    <path d="M 46 29 C 48 26 56 54 34 C 52 41 41 36 46 29 Z"
    fill="{spotFill}" stroke="black"/>
    <path d="M 19 44 C 22 40 37 53 30 63 L 23 63 C 21 63 19 61 19 59 Z" 
    fill="{spotFill}" stroke="black"/>"""
        svgOut = svgOut + spots
    else:
        None

    #-- Body Spots -- 

    if randomiser % 2 == 0:
        spots = f"""
    <!-- Spots -->
    <path d="M 10 66 C 20 67 20 78 10 77 C 0 76 0 65 10 66 Z"
    fill="{spotFill}" stroke="black"/>
    <path d="M 4 55 C 0 62 15 63 14 55 Z" 
    fill="{spotFill}" stroke="black"/>"""
        svgOut = svgOut + spots
    else:
        None

    svgOut = svgOut + "\n</svg>"
    print(svgOut)
    svg2png(bytestring=svgOut,write_to=filename)
    count += 1
