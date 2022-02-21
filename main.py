#-- Imports --
import math
import os
import random
import time

from cairosvg import svg2png  # CairoSvg - converts `.svg` to `.png`

#-- Makes directory `HAWSIES` if not exists --
if os.path.isdir("HAWSIES"):
    os.chdir("HAWSIES")
else:
    os.mkdir("HAWSIES")
    os.chdir("HAWSIES")
count = 0

#-- Timer start -- 
start = time.time()

#-- Main Program --
while count <= 999:
    
    formatNum =  '{:03}'.format(count) # Sets number
    filename = f"hawsie #{formatNum}.png" # Sets filename
    print(filename) # Returns Filename

    #-- Set xml version/ encoding etc
    svgOut = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg height="1600" width="1600">
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
    <path d="M 0 0 L 1600 0 L 1600 1600 L 0 1600 Z"
    fill="{backgroundColour}" stroke="Black" stroke-width="0px"/>"""
    
    svgOut = svgOut + background

    #-- Face --

    furColour = colourGen(None)

    face = f"""
    <!-- Face -->
    <path d="M 300 300 L 380 80 L 460 300 L 540 80 L 620 300 L 1220 300 C 1260 300 1300 340 1300 380 L 1300 780 L 780 780 C 760 780 740 800 740 820 L 740 1160 C 740 1180 760 1200 780 1200 L 1300 1200 C 1300 1260 1260 1300 1200 1300 L 400 1300 C 340 1300 300 1260 300 1200 Z" 
    fill="{furColour}" stroke="black" stroke-width="0.5" />"""
    
    svgOut = svgOut + face
    
    #-- Body --

    body = f"""
    <!-- Body -->
    <path d="M 300 1100 L -20 1100 L -20 1620 L 540 1620 L 540 1300 L 400 1300 C 340 1300 300 1260 300 1200 Z" 
    fill="{furColour}" stroke="black" stroke-width="0.5" />"""

    svgOut = svgOut + body

    #-- Ears --

    ears = """<!-- Ears -->
    <path d="M 320 300 L 380 140 L 440 300 Z M 480 300 L 540 140 L 600 300 Z"
    fill="#ffbec1" stroke="black" stroke-width="0.5" />"""

    svgOut = svgOut + ears

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
    <!-- Outer -->
    <path d="M 540 500 C 540 440 560 380 620 380 C 680 380 700 440 700 500 C 700 560 680 620 620 620 C 560 620 540 560 540 500 C 540 440 520 380 460 380 C 400 380 380 440 380 500 C 380 560 400 620 460 620 C 520 620 540 560 540 500 Z"
        fill="{eyeColour}" stroke="black" stroke-width="0.5"/>
    <!-- Pupils -->
    <path d="M 440 520 C 440 500 440 460 480 460 C 520 460 520 500 520 520 C 520 540 520 580 480 580 C 440 580 440 540 440 520 Z"
        fill="black" stroke="black" stroke-width="0.5"/>
    <path d="M 600 520 C 600 500 600 460 640 460 C 680 460 680 500 680 520 C 680 540 680 580 640 580 C 600 580 600 540 600 520 Z"
        fill="black" stroke="black" stroke-width="0.5"/>"""    
    
    svgOut = svgOut + eyes

    #-- File Writing + Finalising --

    svgOut = svgOut + "\n</svg>"
    print(svgOut)
    svg2png(bytestring=svgOut,write_to=filename)
    count += 1

end = time.time()

timer = end-start

print(f"""
===========================================

Time Taken to make 1000 images:
{round(timer, 4)} s
---------------------------------
Time taken per image:
~ {round(timer/1000,4)} s""")
