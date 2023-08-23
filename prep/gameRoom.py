import numpy as np
from vpython import *


wall_length=10
wall_width=10
wall_height=10
wall_thickness=wall_length*0.01
ball_radius=wall_thickness*5
displacement=5
left_wall=box(pos=vector(-displacement,0,0),
                color=color.cyan,
                length=wall_thickness,
                width=wall_width,
                height=wall_height)
right_wall=box(pos=vector(displacement,0,0),
                color=color.white,
                length=wall_thickness,
                width=wall_width,
                height=wall_height)
back_wall=box(pos=vector(0,0,-displacement),
                color=color.magenta,
                length=wall_length,
                width=wall_thickness,
                height=wall_height)
top_wall=box(pos=vector(0,displacement,0),
                color=color.yellow,
                length=wall_length,
                width=wall_width,
                height=wall_thickness)
bottom_wall=box(pos=vector(0,-displacement,0),
                color=color.white,
                length=wall_length,
                width=wall_width,
                height=wall_thickness)
ball=sphere(radius=ball_radius,
                color=color.red)

while True:
    pass