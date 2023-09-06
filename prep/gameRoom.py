import numpy as np
from vpython import *
import serial
import time
import os

arduinoData=serial.Serial('com4',115200)

wall_lengthX=12
wall_heightY=10
wall_widthZ=16
wall_thickness=.5
wall_color=vector(1,1,1)
ball_color=vector(0,0,1)
wall_opacity=.8
front_opacity=.1
ball_radius=.5

paddleX=2
paddleY=2
paddleZ=.2
paddleOpacity=.8
paddleColor=vector(0,.8,6)

blocking_wall_color=vector(1,1,0)
blocking_wall_opacity=.6

score=0

left_wall=box(pos=vector(-wall_lengthX/2,0,0),
                color=wall_color,
                size=vector(wall_thickness,wall_heightY,wall_widthZ),
                opacity=wall_opacity)
right_wall=box(pos=vector(wall_lengthX/2,0,0),
                color=wall_color,
                size=vector(wall_thickness,wall_heightY,wall_widthZ),
                opacity=wall_opacity)
back_wall=box(pos=vector(0,0,-wall_widthZ/2),
                size=vector(wall_lengthX,wall_heightY,wall_thickness),
                color=wall_color,
                opacity=wall_opacity)
front_wall=box(pos=vector(0,0,wall_widthZ/2),
                size=vector(wall_lengthX,wall_heightY,wall_thickness),
                color=wall_color,
                opacity=front_opacity)
ceiling_wall=box(pos=vector(0,wall_heightY/2,0),
                size=vector(wall_lengthX,wall_thickness,wall_widthZ),
                opacity=wall_opacity,
                color=wall_color)
floor_wall=box(pos=vector(0,-wall_heightY/2,0),
                size=vector(wall_lengthX,wall_thickness,wall_widthZ),
                color=wall_color,
                opacity=wall_opacity)
ball=sphere(radius=ball_radius,
                color=ball_color)
paddle=box(size=vector(paddleX,paddleY,paddleZ),
            pos=vector(0,0,wall_widthZ/2),
            color=paddleColor,
            opacity=paddleOpacity)
blocking_wall=box(pos=vector(0,0,wall_widthZ/2),
                size=vector(wall_lengthX,wall_heightY,wall_thickness),
                color=blocking_wall_color,
                opacity=blocking_wall_opacity)
score_label=label(Text=score)

def add_scores(point):
    global score
    score = score + point
    score_label.text=score
def show_blocking_wall():
    blocking_wall.visible = True

def hide_blocking_wall():
    blocking_wall.visible = False

ballX=0
deltaX=.1

ballY=0
deltaY=.1

ballZ=0
deltaZ=.1

while True:
    
    while arduinoData.inWaiting() == 0:
        pass
    dataPacket = arduinoData.readline() 
    print(dataPacket)
    dataPacket=str(dataPacket,'utf-8')
    dataPacket.strip('\r\n')
    splitPacket=dataPacket.split(',')

    x=float(splitPacket[0])
    y=float(splitPacket[1])
    z=float(splitPacket[2])

    padX=(wall_lengthX/1023.)*x-wall_lengthX/2
    padY=(-wall_heightY/1023.)*y+(wall_heightY/2)

    ballX=ballX+deltaX
    ballY=ballY+deltaY
    ballZ=ballZ+deltaZ
    if z == 1:
        hide_blocking_wall()
    if z == 0:
        show_blocking_wall()
    if ballX+ball_radius > (wall_lengthX/2-wall_thickness/2) or ballX-ball_radius < (-wall_lengthX/2+wall_thickness/2):
        deltaX=deltaX*(-1)
        ballX=ballX+deltaX

    if ballY+ball_radius > (wall_heightY/2-wall_thickness/2) or ballY-ball_radius < (-wall_heightY/2+wall_thickness/2):
        deltaY=deltaY*(-1)
        ballY=ballY+deltaY

    if  ballZ-ball_radius < (-wall_widthZ/2+wall_thickness/2):
        deltaZ=deltaZ*(-1)
        ballZ=ballZ+deltaZ
    
    if ballZ+ball_radius>=wall_widthZ/2-wall_thickness/2:
        if ballX>padX-paddleX/2 and ballX<padX+paddleX/2 and ballY>padY-paddleY/2 and ballY<padY+paddleY/2:
            deltaZ=deltaZ*(-1)
            ballZ=ballZ+deltaZ
            add_scores(1)
        elif z==0:
            deltaZ=deltaZ*(-1)
            ballZ=ballZ+deltaZ
            add_scores(1)
        else:
            lb=label(text="GAME OVER !!!")
            time.sleep(2)
            os._exit(0)



    ball.pos=vector(ballX,ballY,ballZ)
    paddle.pos=vector(padX,padY,wall_widthZ/2)
    pass