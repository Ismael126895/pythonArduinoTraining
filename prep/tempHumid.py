import time
import serial
from vpython import *
import numpy as np

scene.center=vector(5,0,0)
scene.width=1000
scene.height=600
mercury_radius=1
mercury_length=6
digital_thermometer_value=label(text='50',
                    height=20,
                    box=False,
                    pos=vector(1.0,-2.5,2))
digital_humidity_value=label(text='50',
                    height=20,
                    box=False,
                    pos=vector(7,-2.5,2))
mercury_tube=cylinder(pos=vector(0,-3,0),
                    radius=mercury_radius*.6,
                    length=mercury_length,
                    color=color.red,
                    opacity=1,
                    axis=vector(0,1,0))
mercury_bulb=sphere(pos=vector(0,-3,0),
                   radius=mercury_radius,
                   color=color.red,
                  opacity=1,
                   axis=vector(0,1,0))
glass_bulb=sphere(radius=mercury_radius*1.2,
                    pos=vector(0,-3,0),
                    length=mercury_length,
                    color=color.white,
                    opacity=.3,
                    axis=vector(0,1,0))
glass_tube=cylinder(pos=vector(0,-3,0),
                    radius=mercury_radius*.8,
                    length=mercury_length,
                    color=color.white,
                    axis=vector(0,1,0),
                    opacity=.3)
for temp in range(0,100,10):
    tickPos = 9*temp/200.+1.5
    tick=cylinder(color=color.black,
                    radius=.8,
                    length=.1,
                    axis=vector(0,1,0),
                    pos=vector(0,tickPos-3,0))  
    label=text(color=color.white,
                text=str(temp),
                pos=vector(-2,tickPos-3,0),
                height=.3)

boxX=10
boxY=6
boxZ=.4
offset_right=boxX/2+2
my_case=box(size=vector(boxX,boxY,boxZ),
            color=color.white,
            pos=vector(offset_right,0,-boxZ/2))
arrow_length=boxY-2
arrow_thickness=.1
arrow_z_offset=.25
my_arrow=arrow(length=arrow_length,
                color=color.red,
                shaftwidth=arrow_thickness,
                pos=vector(offset_right,-.9*boxY/2,arrow_z_offset))
tick_length=.4
tick_width=.07
tick_height=.07
tick_factor=.7

for theta in np.linspace(5*np.pi/6,np.pi/6,11):
    tick_major=box(pos=vector(1.1*arrow_length*np.cos(theta)+offset_right,1.1*arrow_length*np.sin(theta)-.9*boxY/2,0),
                   size=vector(tick_length,tick_width,tick_height),
                   color=color.black,
                   axis=vector(arrow_length*np.cos(theta),arrow_length*np.sin(theta),0) )
for theta in np.linspace(5*np.pi/6,np.pi/6,51):
    tick_minor=box(pos=vector(1.1*arrow_length*np.cos(theta)+offset_right,1.1*arrow_length*np.sin(theta)-.9*boxY/2,0),
                   size=vector(tick_factor*tick_length,tick_factor*tick_width,tick_factor*tick_height),
                   color=color.black,
                   axis=vector(arrow_length*np.cos(theta),arrow_length*np.sin(theta),0) )
num=0
for theta in np.linspace(5*np.pi/6,np.pi/6,11):
    no_label=text(text=str(num),
                pos=vector(1.2*arrow_length*np.cos(theta)+offset_right,1.2*arrow_length*np.sin(theta)-.9*boxY/2,0),
                axis=vector(arrow_length*np.cos(theta-np.pi/2),arrow_length*np.sin(theta-np.pi/2),0),
                color=color.black,
                height=.4,
                align='center')
    num=num+10
arduinoData=serial.Serial('com4',115200)
time.sleep(.5)
while True:
    while arduinoData.inWaiting()==0:
        pass
    dataHolder=arduinoData.readline()
    dataHolder=str(dataHolder,'utf-8')
    dataHolder=dataHolder.strip('\r\n')
    dataHolder=dataHolder.split(",")

    temp=float(dataHolder[1])
    hum=float(dataHolder[2])
    mercury_length=9*temp/200.+1.5
    theta=-np.pi/150.*hum + 5*pi/6

    mercury_tube.length=mercury_length
    digital_thermometer_value.text=temp
    digital_humidity_value.text=hum
    my_arrow.axis=vector(arrow_length*np.cos(theta),arrow_length*np.sin(theta),0)
    print(dataHolder[1])
