#-- Imports --
import base64
import csv
import math
import os
import random
import sys
import time
from datetime import date, datetime

import requests
from cairosvg import svg2png  # CairoSvg - converts `.svg` to `.png`
from PIL.PngImagePlugin import PngImageFile, PngInfo
from simple_chalk import (black, blue, blueBright,  # Colours terminal text
                          green, red, yellow)

darkred = black.bgRed
total_size = 0
#-- Makes directory `HAWSIES` if not exists --
if os.path.isdir("HAWSIES"):
    os.chdir("HAWSIES")
else:
    os.mkdir("HAWSIES")
    os.chdir("HAWSIES")

#-- CONSTANTS--
count = 0

LINE_WEIGHT = 10
TEMP_SVG =""
TODAY = date.today()
TODAY = TODAY.strftime("%d-%m-%Y")

logTableData = ""

#-- open log csv

logcsv = open("log.csv","a")
logcsv.write(f"""Number,"Fur Colour","Spot Colour","Eye Colour",glassesTrue,Glasses Colour,Date Made,Time Made\n""")

#-- Generate random colour --

def colourGen(darkerTrue=None): #,hex_=None
    colour = ""
    r = random.randint(55,200)
    g = random.randint(55,200)
    b = random.randint(55,200)
    if darkerTrue == None:#and hex_ == 
        colour = f"rgb({r},{g},{b})"
    """ 
    if hex_:
        r = hex(int(r))
        g = hex(int(g))
        b = hex(int(b))
        str(r).replace("0x", "")
        str(g).replace("0x", "")
        str(b).replace("0x", "")
        colour = f"#{str(r)}{str(g)}{str(b)}"
""" 
    if darkerTrue:
        r = r * 0.25
        g = g * 0.25
        b = b * 0.25
        colour = f"rgb({r},{g},{b})"

    return colour


def createElem(path,name,colour=None,strokeColour="Black",strokeWeight=LINE_WEIGHT,DarkerTrue=None,text=""):
    
    elementColour = colourGen(DarkerTrue)
    if text != "":
        end = f">{text}</path>"
    else:
        end = "/>"
    element = f"""<!-- {name} -->
        <path d="{path}"
        fill="{elementColour}" stroke="{strokeColour}" stroke-width="{strokeColour}" {end}"""
    return element

""" 
def invertHex(hex_):
    if hex_[0] == "#":
        hex_.replace(hex_[0],"")
    int(hex_) ** 255
    str(r).replace("0x", "")
    str(g).replace("0x", "")
    str(b).replace("0x", "") """   


"""def invertColor(hex_):
    hex_ = hex_[1,len(hex_)]
    #invert color components
    r = str(255 - int(hex_[0, 2]))
    g = str(255 - int(hex_[2, 4]))
    b = str(255 - int(hex_[4, 6]))
    #pad each with zeros and return
    return '#' + '{:01}'.format(r) + '{:01}'.format(g) + '{:01}'.format(b)"""

###########################################################################################



#-- Main Program --
global debug

run = input("Run program okay? y/N \n> ")
if run.lower() == "y":
    run = True
    print(f"Input the number of Hawsies you want.")
    print(red("The more made, the longer it will take."))
    numberCalled = int(input("\n> "))-1
    debug = False
elif run.lower() == "n":
    time.sleep(10)
    quit()
elif run.lower == "y -d":
    debug = True
    run = True

while run:  
    #-- Timer start -- 
    start = time.time()
    while count <= numberCalled:
        subTimer = time.time()    
        formatNum =  '{:03}'.format(count) # Sets number
        filename = f"hawsie #{formatNum}" # Sets filename
        print(yellow(f"Creating `{filename}`...")) # Returns Filename

        # global targetImage
        # targetImage = PngImageFile(f"{filename}.png")

        # metadata = PngInfo()
        # metadata.add_text("File", f"{filename}")

        #-- Set xml version/ encoding etc
        svgOut = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
        <!-- 
        Hawsie number #{formatNum}.
        Made on {TODAY} at {datetime.now()}-->
    <svg height="1600" width="1600">
    """

        #-- Background --

        backgroundColour = colourGen()

        # createElem("M 0 0 L 1600 0 L 1600 1600 L 0 1600 Z", "Background", )

        background = f"""<!-- Background -->
        <path d="M 0 0 L 1600 0 L 1600 1600 L 0 1600 Z"
        fill="{backgroundColour}" stroke="Black" stroke-width="0px"/>"""
        
        svgOut = svgOut + background

        #-- Face --

        furColour = colourGen()

        face = f"""
        <!-- Face -->
        <path d="M 300 300 L 460 80 L 460 300 L 620 80 L 620 300 L 1220 300 C 1260 300 1300 340 1300 380 L 1300 780 L 780 780 C 760 780 740 800 740 820 L 740 1160 C 740 1180 760 1200 780 1200 L 1300 1200 C 1300 1260 1260 1300 1200 1300 L 400 1300 C 340 1300 300 1260 300 1200 Z" 
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
        <path d="M 320 300 L 440 140 L 440 300 Z M 480 300 L 600 140 L 600 300 Z"
        fill="#ffbec1" stroke="black" stroke-width="{LINE_WEIGHT}" />"""

        svgOut = svgOut + ears

        #-- Face Spots --

        randomiser = random.randint(0, 99)
        spotsFill = colourGen(True)
        if randomiser % 2 == 0:
            spotsTrue = "YES"
            spots = f"""
            <!-- Spots -->
        <path d="M 300 840 C 500 840 700 1160 600 1300 L 400 1300 C 340 1300 300 1260 300 1200 M 860 300 C 700 460 1260 640 1140 300 Z"
        fill="{spotsFill}" stroke="black" stroke-width="{LINE_WEIGHT}" />"""
            svgOut = svgOut + spots
        else:
            None

        #-- Body Spots -- 

        if randomiser % 2 == 0:
            spotsTrue = "YES"
            spots = f"""
        <!-- Spots -->
        <path d="M 62 1100 C 183 1266 45 1342 0 1318 L 0 1100 Z M 103 1480 C 51 1394 255 1345 345 1435 C 410 1500 151 1551 103 1480 Z" 
        fill="{spotsFill}" stroke="black" stroke-width="{LINE_WEIGHT}" />"""
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
            glassesTrue = True
            glassesFill=random.randint(0,9)
            
            glassesColours = ["aliceblue","antiqueWhite","cadetblue","darkolivegreen","darkseagreen","darkslategrey","darkmagenta","darkred","goldenrod","hotpink"]
            glassesFill = glassesColours[glassesFill]
            glasses = f"""<!-- Glasses -->
            <path d="M 295 400 L 715 400 L 715 520 C 715 620 540 620 540 530 C 540 640 365 620 365 520 L 365 420 L 295 420 L 295 420 L 295 400 M 385 420 L 385 520 C 385 600 530 610 530 510 L 530 420 Z M 550 420 C 550 450 550 480 550 510 C 550 610 695 610 695 510 L 695 420 Z"
            fill="{glassesFill}" stroke="black" stroke-width="{LINE_WEIGHT}"/>"""

            
            svgOut = svgOut + glasses
        else:
            glassesTrue = False
            glassesFill = None

        
        textColour = ["aliceblue","antiqueWhite","cadetblue","darkolivegreen","darkseagreen","darkslategrey","darkmagenta","darkred","goldenrod","hotpink"]
        textFill = textColour[random.randint(0,9)]
        text = f"""<text style="vertical-align:top; text-align:right fill={textFill}; font-size=10px">{filename}</text>"""

        svgOut = svgOut + createElem("""M 500 245 C 498 241 490 241 485 245 C 482 243 490 229 494 232 C 480 226 471 217 460 244 L 460 300 Z 
        M 340 245 C 328 250 332 234 300 243 C 311 234 296 221 318 210 C 274 227 270 235 259 257 C 236 290 193 214 225 329 C 210.3333 331.3333 199 381 173 302 C 161.3333 338 149.6667 374 204 469 C 190 488 185 523 141 466 C 169 547 128 537 206 634 C 184.3333 649.3333 162.6667 664.6667 127 618 C 147 679 126 717 227 757 C 210 785 201 828 133 798 C 143 844 180 885 216 918 C 191 907 159 933 127 895 C 150.6667 931.3333 132 970 198 1004 C 183 1014 197 1084 132 1007 C 137 1042 152 1079 173 1100 L 300 1100 L 300 300 Z 
        M 760 300 C 796 262 735 255 777 219 C 720 230 703 213 648 239 C 659 221 647 228 676 203 C 649 207 630 222 620 240 L 620 300 Z""", "Mane", DarkerTrue=True, strokeColour="Black")

        #-- File Writing + Finalising --

        svgOut = svgOut + "\n</svg>"

        svg2png(bytestring=svgOut,write_to=f"{filename}.png")
        count += 1

        """if not(debug == None or debug == False):
            with open(f"{filename}.svg", "w") as g:
                g.write(svgOut)
                g.close()
            print(f"`{filename}.svg` created also.")"""
        total_size = int(os.path.getsize(f"{filename}.png"))
        
        subTimerEnd = time.time()

        if count == 1:
            # with open("hawsie_template.svg","w") as f:
            #     f.write(svgOut)
            svgOut = TEMP_SVG
            

        logTableData += f"""{formatNum},"{furColour}","{spotsFill}","{eyeColour}",{bool(glassesTrue)},{glassesFill},{TODAY},{time.time()}\n"""

        """with open("hawsieLog.txt", "a") as f:
            os.chdir("..")
            f.write(f""==================== {formatNum} ====================
            {TODAY}
            {filename} created at {subTimer}, writing finished {round(subTimerEnd - subTimer, 4)} s later at {time.time()}.
            SVG File:
            --------------------------------------

            {svgOut}
            
            "")
            os.chdir("HAWSIES")"""

        # targetImage.save("NewPath.png", pnginfo=metadata)
        # targetImage = PngImageFile(f"{filename}.png")

        # print(targetImage.text)

        print(f"`{green(filename)}.png` created in {blue(round(subTimerEnd - subTimer, 4))} s")


        with open(f"{filename}.png", "rb") as file:
            url = "https://api.imgbb.com/1/upload"
            payload = {
                "key": "02d0dcd27fdef5a9f31c250046ba59f8",
                "image": base64.b64encode(file.read()),
            }
        res = requests.post(url, payload)

        
        
    """os.replace("/HAWSIES/hawsieLog.txt", f"hawsieLog_{TODAY}.txt")"""
    end = time.time()

    timer = end-start

    print(f"""

=========================================

Time Taken to make {count} images: {blue(round(timer, 4))} s
----------------------------------------
Avg. time taken per image: ~ {blue(round(timer/1000,4))} s

Total file size: {red(total_size)} bytes


{res}""")
    

    # svg2png(bytestring=TEMP_SVG,write_to="hawsie_template.png")

    # with open("temp.svg","w") as f:
    #     f.write(TEMP_SVG)


    logcsv.write(logTableData + "\n")
    print(blueBright("log table written"))
    run = not(run)
