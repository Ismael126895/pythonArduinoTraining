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
for theta in np.linspace(5*np.pi/6,np.pi/6,6):
    tickMajor=box(color=color.black,pos=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0),size=vector(tickL,tickW,tickH),axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0))
for theta in np.linspace(5*np.pi/6,np.pi/6,50):
    tickMinor=box(color=color.black,pos=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0),size=vector(tickL/2,tickW/2,tickH/2),axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0))

boxX=2.5
boxY=1.5
boxZ=.1
myCase=box(color=color.white,size=vector(boxX,boxY,boxZ),pos=vector(0,.9*boxY/2,-boxZ))
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
   