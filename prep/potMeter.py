import time
import serial
from vpython import *
arduinoData=serial.Serial('com4',115200)
time.sleep(1)
tube=cylinder(color=color.blue,radius=1,length=1,axis=vector(0,1,0))
lab=label(text='10k Ohm resistor',box=False,pos=vector(0,.1,0))
while True:
    while(arduinoData.inWaiting()==0):
        pass    
    dataPacket=arduinoData.readline()
    dataPacket=str(dataPacket,'utf-8')
    dataPacket=int(dataPacket.strip('\r\n'))
    potVal=dataPacket
    res=(10000./1023.)*potVal
    if res==0:
        res=.001
    tube.length=res/10000.
    res=round(res,1)
    lab.text=str(res)

    