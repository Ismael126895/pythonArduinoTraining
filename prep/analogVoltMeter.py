import time
import serial
from vpython import *
import numpy as np

tickL=.1
tickW=.02
tickH=.02
arrowLength=1
arrowWidth=.02
myArrow=arrow(length=arrowLength,shaftwidth=arrowWidth,color=color.red,axis=vector(0,1,0))
hubL=.02
hubR=.02
hub=cylinder(color=color.red,radius=hubR,length=hubL,axis=vector(0,0,1))
for theta in np.linspace(5*np.pi/6,np.pi/6,6):
    tickMajor=box(color=color.black,pos=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0),size=vector(tickL,tickW,tickH),axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0))
tickFraction=.5
for theta in np.linspace(5*np.pi/6,np.pi/6,50):
    tickMinor=box(color=color.black,pos=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0),size=vector(tickFraction*tickL,tickFraction*tickW,tickFraction*tickH),axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0))
cnt=0
labF=1.1
for theta in np.linspace(5*np.pi/6,np.pi/6,6):
    lab=text(text=str(cnt),pos=vector(labF*arrowLength*np.cos(theta),labF*arrowLength*np.sin(theta),0),color=color.black,height=.1,align='center',axis=vector(arrowLength*np.cos(theta-np.pi/2),arrowLength*np.sin(theta-np.pi/2),0))
    cnt=cnt+1

boxX=2.5
boxY=1.75
boxZ=.1
myCase=box(color=color.white,size=vector(boxX,boxY,boxZ),pos=vector(0,.9*boxY/2,-boxZ))
myLabel=text(text='voltOmatic',pos=vector(0,1.25,0),color=color.red, height=.2, align='center')
arduinoData=serial.Serial('com4',115200)
time.sleep(1)
while True:
    
    while arduinoData.in_waiting==0:
        pass
    dataPacket=arduinoData.readline()
    dataPacket=str(dataPacket,'utf-8')
    dataPacket=dataPacket.strip('\r\n')
    dataPacket=int(dataPacket)
    potVal=dataPacket
    theta=-2*np.pi*potVal/3096+5*np.pi/6
    myArrow.axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0)
    # for theta in np.linspace(5*np.pi/6,np.pi/6,150):
    #     rate(100)
    #     myArrow.axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0)
    # for theta in np.linspace(np.pi/6,5*np.pi/6,150):
    #     rate(100)
    #     myArrow.axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0)
   