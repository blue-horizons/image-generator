#-- Imports --
import math
import os
import random

from cairosvg import svg2png # CairoSvg - converts `.svg` to `.png` 

#-- Makes directory `HAWSIES` if not exists --
if os.path.isdir("HAWSIES"):
    os.chdir("HAWSIES")
else:
    os.mkdir("HAWSIES")
    os.chdir("HAWSIES")
count = 0




#-- Main Program --
while count <= 999:
    
    formatNum =  '{:03}'.format(count) # Sets number
    filename = f"hawsie #{formatNum}.png" # Sets filename
    print(filename) # Returns Filename

    #-- Set xml version/ encoding etc
    svgOut = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg height="86" width="86">
"""

    #generate random colour

    def colourGen(darkerTrue):
        colour = ""
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

    backgroundColour = colourGen(None)

    background = f"""<!-- Background -->
    <path d="M 0 0 L 80 0 L 80 80 L 0 80 Z"
    fill="{backgroundColour}" stroke="Black" stroke-width="0px"/>"""
    
    svgOut = svgOut + background

    #-- Face --

    furColour = colourGen(None)

    face = f"""
    <!-- Face -->
    <path d="M 15 15 L 19 4 L 23 15 L 27 4 L 31 15 L 61 15 C 63 15 65 17 65 19 L 65 39 L 39 39 C 38 39 37 40 37 41 L 37 58 C 37 59 38 60 39 60 L 65 60 C 65 63 63 65 60 65 L 20 65 C 17 65 15 63 15 60 Z M 0 0 L 80 0 L 80 80 L 0 80 Z M 16 15 L 19 6 L 22 15 Z" 
    fill="{furColour}" stroke="black" stroke-width="0.5" />"""
    
    svgOut = svgOut + face
    
    #-- Body --

    body = f"""
    <!-- Body -->
    <path d="M 24 15 L 27 6 L 30 15 Z M 15 45 L -1 45 L -1 82 L 25 82 L 25 65 L 20 65 C 17 65 15 63 15 60 Z" 
    fill="{furColour}" stroke="black" stroke-width="0.5" />"""

    svgOut = svgOut + body

    #-- Face Spots --

    randomiser = random.randint(0, 99)
    spotFill = colourGen(True)
    if randomiser % 2 == 0:
        spots = f"""
        <!-- Spots -->
    <path d="M 15 42 C 25 42 35 58 30 65 L 20 65 C 17 65 15 63 15 60 M 43 15 C 35 23 63 32 57 15 Z"
    fill="{spotFill}" stroke="black"/>"""
        svgOut = svgOut + spots
    else:
        None

    #-- Body Spots -- 

    if randomiser % 2 == 0:
        spots = f"""
    <!-- Spots -->
    <path d="M 3 45 C 1 52 9 68 15 59 L 15 45 M 25 70 C 18 67 3 74 5 80 L 25 80 Z" 
    fill="{spotFill}" stroke="black"/>"""
        svgOut = svgOut + spots
    else:
        None


    #-- Eyes --

    eyeColour = colourGen(None)

    eyes = f"""
    <!-- Eyes -->
    <!-- Whites -->
    <path d="M -13 -15 C -13 -18 -12 -21 -9 -21 C -6 -21 -5 -18 -5 -15 C -5 -12 -6 -9 -9 -9 C -12 -9 -13 -12 -13 -15 C -13 -18 -14 -21 -17 -21 C -20 -21 -21 -18 -21 -15 C -21 -12 -20 -9 -17 -9 C -14 -9 -13 -12 -13 -15 Z"
        fill="{eyeColour}" stroke="black" stroke-width="0.5"/>
    <!-- Pupils -->
    <path d="M -18 -14 C -18 -15 -18 -17 -16 -17 C -14 -17 -14 -15 -14 -14 C -14 -13 -14 -11 -16 -11 C -18 -11 -18 -13 -18 -14 Z"
        fill="black" stroke="black" stroke-width="0.5"/>
    <path d="M -10 -14 C -10 -15 -10 -17 -8 -17 C -6 -17 -6 -15 -6 -14 C -6 -13 -6 -11 -8 -11 C -10 -11 -10 -13 -10 -14 Z"
        fill="black" stroke="black" stroke-width="0.5"/>"""    
    
    svgOut = svgOut + eyes

    #-- File Writing + Finalising --

    svgOut = svgOut + "\n</svg>"
    print(svgOut)
    svg2png(bytestring=svgOut,write_to=filename)
    count += 1

