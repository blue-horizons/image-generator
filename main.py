#-- Imports --
import math
import os
import random
import time
from datetime import date

from cairosvg import svg2png  # CairoSvg - converts `.svg` to `.png`

#-- Makes directory `HAWSIES` if not exists --
if os.path.isdir("HAWSIES"):
    os.chdir("HAWSIES")
else:
    os.mkdir("HAWSIES")
    os.chdir("HAWSIES")
count = 0

LINE_WEIGHT = 10

#generate random colour

def colourGen(darkerTrue=None):
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

#-- Timer start -- 
start = time.time()

#-- Main Program --
while count <= 999:
    os.chdir("HAWSIES")
    subTimer = time.time()    
    formatNum =  '{:03}'.format(count) # Sets number
    filename = f"hawsie #{formatNum}.png" # Sets filename
    print(f"Creating `{filename}`...") # Returns Filename

    #-- Set xml version/ encoding etc
    svgOut = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg height="1600" width="1600">
"""

    #-- Background --

    backgroundColour = colourGen()

    background = f"""<!-- Background -->
    <path d="M 0 0 L 1600 0 L 1600 1600 L 0 1600 Z"
    fill="{backgroundColour}" stroke="Black" stroke-width="0px"/>"""
    
    svgOut = svgOut + background

    #-- Face --

    furColour = colourGen()

    face = f"""
    <!-- Face -->
    <path d="M 300 300 L 380 80 L 460 300 L 540 80 L 620 300 L 1220 300 C 1260 300 1300 340 1300 380 L 1300 780 L 780 780 C 760 780 740 800 740 820 L 740 1160 C 740 1180 760 1200 780 1200 L 1300 1200 C 1300 1260 1260 1300 1200 1300 L 400 1300 C 340 1300 300 1260 300 1200 Z" 
    fill="{furColour}" stroke="black" stroke-width="{LINE_WEIGHT}" />"""
    
    svgOut = svgOut + face
    
    #-- Body --

    body = f"""
    <!-- Body -->
    <path d="M 300 1100 L -20 1100 L -20 1620 L 540 1620 L 540 1300 L 400 1300 C 340 1300 300 1260 300 1200 Z" 
    fill="{furColour}" stroke="black" stroke-width="{LINE_WEIGHT}" />"""

    svgOut = svgOut + body
    
    #-- Teeth --

    teeth = f"""<!-- Teeth -->
    <path d="M 1295 780 C 1295 825 1220 825 1220 780 C 1220 825 1145 825 1145 780 C 1145 825 1070 825 1070 780 C 1070 825 995 825 995 780 C 995 825 920 825 920 780 C 920 825 845 825 845 780 Z M 1295 1200 C 1295 1155 1220 1155 1220 1200 C 1220 1155 1135 1155 1135 1200 C 1135 1155 1060 1155 1060 1200 C 1060 1155 985 1155 985 1200 C 985 1155 910 1155 910 1200 C 910 1155 835 1155 835 1200 Z"
    fill="white" stroke="black" stroke-width="{LINE_WEIGHT}"/>"""
    
    svgOut = svgOut + teeth
    #-- Ears --

    ears = f"""<!-- Ears -->
    <path d="M 320 300 L 380 140 L 440 300 Z M 480 300 L 540 140 L 600 300 Z"
    fill="#ffbec1" stroke="black" stroke-width="{LINE_WEIGHT}" />"""

    svgOut = svgOut + ears

    #-- Face Spots --

    randomiser = random.randint(0, 99)
    spotFill = colourGen(True)
    if randomiser % 2 == 0:
        spotsTrue = "YES"
        spots = f"""
        <!-- Spots -->
    <path d="M 300 840 C 500 840 700 1160 600 1300 L 400 1300 C 340 1300 300 1260 300 1200 M 860 300 C 700 460 1260 640 1140 300 Z"
    fill="{spotFill}" stroke="black" stroke-width="{LINE_WEIGHT}" />"""
        svgOut = svgOut + spots
    else:
        None

    #-- Body Spots -- 

    if randomiser % 2 == 0:
        spotsTrue = "YES"
        spots = f"""
    <!-- Spots -->
    <path d="M 62 1100 C 183 1266 45 1342 0 1318 L 0 1100 Z M 103 1480 C 51 1394 255 1345 345 1435 C 410 1500 151 1551 103 1480 Z" 
    fill="{spotFill}" stroke="black" stroke-width="{LINE_WEIGHT}" />"""
        svgOut = svgOut + spots
    else:
        None

    #-- Eyes --

    eyeColour = colourGen()

    eyes = f"""
    <!-- Eyes -->
    <!-- Outer -->
    <path d="M 540 500 C 540 440 560 380 620 380 C 680 380 700 440 700 500 C 700 560 680 620 620 620 C 560 620 540 560 540 500 C 540 440 520 380 460 380 C 400 380 380 440 380 500 C 380 560 400 620 460 620 C 520 620 540 560 540 500 Z"
        fill="{eyeColour}" stroke="black" stroke-width="{LINE_WEIGHT}"/>
    <!-- Pupils -->
    <path d="M 440 520 C 440 500 440 460 480 460 C 520 460 520 500 520 520 C 520 540 520 580 480 580 C 440 580 440 540 440 520 Z"
        fill="black" stroke="black" stroke-width="{LINE_WEIGHT}"/>
    <path d="M 600 520 C 600 500 600 460 640 460 C 680 460 680 500 680 520 C 680 540 680 580 640 580 C 600 580 600 540 600 520 Z"
        fill="black" stroke="black" stroke-width="{LINE_WEIGHT}"/>"""    
    
    svgOut = svgOut + eyes
    
    #-- Glasses --

    glassesTrue = random.randint(0,100)

    if glassesTrue in range(0,23):
        glassesFill=random.randint(0,9)
        
        glassesColours = ["aliceblue","antiqueWhite","cadetblue","darkolivegreen","darkseagreen","darkslategrey","darkmagenta","darkred","goldenrod","hotpink"]
        glassesFill = glassesColours[glassesFill]
        glasses = f"""<!-- Glasses -->
        <path d="M 295 400 L 715 400 L 715 520 C 715 620 540 620 540 530 C 540 640 365 620 365 520 L 365 420 L 295 420 L 295 420 L 295 400 M 385 420 L 385 520 C 385 600 530 610 530 510 L 530 420 Z M 550 420 C 550 450 550 480 550 510 C 550 610 695 610 695 510 L 695 420 Z"
        fill="{glassesFill}" stroke="black" stroke-width="2"/>"""
        print(glassesFill)
        
        svgOut = svgOut + glasses

    #-- File Writing + Finalising --

    svgOut = svgOut + "\n</svg>"
    svg2png(bytestring=svgOut,write_to=filename)
    count += 1

    subTimerEnd = time.time()

    with open("hawsieLog.txt", "a") as f:
        os.chdir("..")
        f.write(f"""==================== {formatNum} ====================
        {date.today()}
        {filename} created at {subTimer}, writing finished {round(subTimerEnd - subTimer, 4)} s later at {time.time()}.
        SVG File:
        --------------------------------------

        {svgOut}
        
        """)

    #print(f"`{filename}` created in {round(subTimerEnd - subTimer, 4)} s")

end = time.time()

timer = end-start

print(f"""

===========================================

Time Taken to make {count} images:
{round(timer, 4)} s
---------------------------------
Avg. time taken per image:
~ {round(timer/1000,4)} s""")
