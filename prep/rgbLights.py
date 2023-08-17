import serial
from vpython import *
arduinoData=serial.Serial('com4',115200)

baseRadius=1
baseHeight=baseRadius/5
bodyRadius=baseRadius*.75
bodyHeight=2.5*bodyRadius
LEDTopRadius=bodyRadius
LEDTopPos=vector(0,bodyHeight,0)
bulbRadius=bodyRadius*.75
bulbPosition=LEDTopPos
leg1Length=8*bodyRadius
leg2Length=10*bodyRadius
leg3Length=9*bodyRadius
leg4Length=8*bodyRadius
legwidth=baseRadius/10
bulbOpacity=.9
topOpacity=bulbOpacity/2
bottomOpacity=bulbOpacity/2
myColor=vector(10,10,10)
myAxis=vector(0,1,0)

LEDBase=cylinder(length=baseHeight,
                radius=baseRadius,
                color=myColor,
                axis=myAxis,
                opacity=bottomOpacity)
LEDBody=cylinder(length=bodyHeight,
                radius=bodyRadius,
                color=myColor,
                axis=myAxis,
                opacity=bottomOpacity)
LEDTop=sphere(radius=LEDTopRadius,
                color=myColor,
                pos=LEDTopPos,
                axis=myAxis,
                opacity=topOpacity)
bulb=sphere(radius=bulbRadius,
            color=myColor,
            pos=bulbPosition,
            axis=myAxis,
            opacity=bulbOpacity)
leg1=box(color=color.white,
            axis=myAxis,
            pos=vector(-.5*baseRadius,-leg1Length/2+baseHeight,0),
            length=leg1Length,
            width=legwidth,
            height=legwidth)
leg2=box(color=color.white,
            axis=myAxis,
            pos=vector(-.15*baseRadius,-leg2Length/2+baseHeight,0),
            length=leg2Length,
            width=legwidth,
            height=legwidth)
leg3=box(color=color.white,
            axis=myAxis,
            pos=vector(.15*baseRadius,-leg3Length/2+baseHeight,0),
            length=leg3Length,
            width=legwidth,
            height=legwidth)
leg4=box(color=color.white,
            axis=myAxis,
            pos=vector(.5*baseRadius,-leg4Length/2+baseHeight,0),
            length=leg4Length,
            width=legwidth,
            height=legwidth)
head=compound([bulb,LEDBase,LEDBody,LEDTop])

while True:
    
    myCmd=input('Please input your color R:G:B 0-255 ')
    myCmd=myCmd+"\r"
    arduinoData.write(myCmd.encode())
    myColor=myCmd.split(':')
    red=int(myColor[0])
    green=int(myColor[1])
    blue=int(myColor[2])
    head.color=vector(red/255,green/255,blue/255)
    