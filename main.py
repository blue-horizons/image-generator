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

    backgroundColour = colourGen(None)

    background = f"""<!-- Background -->
    <path d="M -40 -40 L 40 -40 L 40 40 L -40 40 Z"
    fill="{backgroundColour}" stroke="Black" stroke-width="0px"/>"""
    
    svgOut = svgOut + background

    #-- Face --

    furColour = colourGen(None)

    face = f"""
    <!-- Face -->
    <path d="M -25 -25 L -21 -36 L -17 -25 L -13 -36 L -9 -25 L 21 -25 C 23 -25 25 -23 25 -21 L 25 -1 L -1 -1 C -2 -1 -3 0 -3 1 L -3 18 C -3 19 -2 20 -1 20 L 25 20 C 25 23 23 25 20 25 L -20 25 C -23 25 -25 23 -25 20 Z" 
    fill="{furColour}" stroke="black" stroke-width="0.5" />"""
    
    svgOut = svgOut + face
    
    #-- Body --

    body = f"""
    <!-- Body -->
    <path d=" M -16 -25 L -13 -34 L -10 -25 Z M -25 5 L -41 5 L -41 42 L -15 42 L -15 25 L -20 25 C -23 25 -25 23 -25 20 Z" 
    fill="{furColour}" stroke="black" stroke-width="0.5" />"""

    svgOut = svgOut + body

    #-- Face Spots --

    randomiser = random.randint(0, 99)
    spotFill = colourGen(True)
    if randomiser % 2 == 0:
        spots = f"""
        <!-- Spots -->
    <path d="M -25 2 C -15 2 -5 18 -10 25 L -20 25 C -23 25 -25 23 -25 20 M 3 -25 C -5 -17 23 -8 17 -25 Z"
    fill="{spotFill}" stroke="black"/>"""
        svgOut = svgOut + spots
    else:
        None

    #-- Body Spots -- 

    if randomiser % 2 == 0:
        spots = f"""
    <!-- Spots -->
    <path d="M -37 5 C -39 12 -31 28 -25 19 L -25 5 M -15 30 C -22 27 -37 34 -35 40 L -15 40 Z" 
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
        fill="{eyeColour}" stroke="black"/>
    <!-- Pupils -->
    <path d="M -18 -14 C -18 -15 -18 -17 -16 -17 C -14 -17 -14 -15 -14 -14 C -14 -13 -14 -11 -16 -11 C -18 -11 -18 -13 -18 -14 Z"
        fill="black" stroke="black"/>
    <path d="M -10 -14 C -10 -15 -10 -17 -8 -17 C -6 -17 -6 -15 -6 -14 C -6 -13 -6 -11 -8 -11 C -10 -11 -10 -13 -10 -14 Z"
        fill="black" stroke="black"/>"""    
    
    svgOut = svgOut + eyes

    #-- File Writing + Finalising --

    svgOut = svgOut + "\n</svg>"
    print(svgOut)
    svg2png(bytestring=svgOut,write_to=filename)
    count += 1
