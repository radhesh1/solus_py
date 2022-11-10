from turtle import position
from ursina import *
import math

def update():
    global t
    t = t + 0.02
    angle = math.pi*40/180
    
    #rotate around the sun
    # radius variable is the distance between the planet and the sun
    # the angle variable is the angle matched by the sun on the Oxygen plane
    # there are 9 planets in all around the sun so 360/9 = 40, each planet is 40 degrees apart, angle has radians
    # variable t is a time variable, i.e. when taking cos, sine of t, each frame of planets will change positions according to the coordinates calculated in t
    # this planet I give distance for being lazy

    radius_1 = 2
    mercury.x = math.cos(t)*radius_1
    mercury.z = math.sin(t)*radius_1

    radius_2 = 5.2
    venus.x = math.cos(t+angle)*radius_2
    venus.z = math.sin(t+angle)*radius_2

    radius_3 = 3.6
    earth.x = math.cos(t+angle*2)*radius_3
    earth.z = math.sin(t+angle*2)*radius_3

    radius_4 = 7.6
    mars.x = math.cos(t+angle*3)*radius_4
    mars.z = math.sin(t+angle*3)*radius_4

    radius_5 = 2.8
    jupiter.x = math.cos(t+angle*4)*radius_5
    jupiter.z = math.sin(t+angle*4)*radius_5

    radius_6 = 6
    saturn.x = math.cos(t+angle*5)*radius_6
    saturn.z = math.sin(t+angle*5)*radius_6

    radius_7 = 8
    uranus.x = math.cos(t+angle*6)*radius_7
    uranus.z = math.sin(t+angle*6)*radius_7

    radius_8 = 4.4
    neptune.x = math.cos(t+angle*7)*radius_8
    neptune.z = math.sin(t+angle*7)*radius_8

    radius_9 = 6.8
    pluto.x = math.cos(t+angle*8)*radius_9
    pluto.z = math.sin(t+angle*8)*radius_9

    #tự xoay quanh trục 
    sun.rotation_y += time.dt*20
    mercury.rotation_y += time.dt*20
    earth.rotation_y += time.dt*20
    venus.rotation_y += time.dt*20
    mars.rotation_y += time.dt*20
    jupiter.rotation_y += time.dt*20
    saturn.rotation_y += time.dt*20
    uranus.rotation_y += time.dt*20
    neptune.rotation_y += time.dt*20
    pluto.rotation_y += time.dt*20

class Sky(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = 'textures/StarsMap_2500x1250.jpg',
            parent = scene,
            scale = 150,
            double_sided = True
        )

app = Ursina()
sku = Sky()
EditorCamera()

sun = Entity(model= "sphere",  scale=3, texture = "textures/2k_sun.jpg")
mercury = Entity(model='obj/Mercury 1K.obj',scale=1, texture = "textures/Diffuse_1K.png")
venus = Entity(model='sphere', scale=0.6, texture = 'textures/2k_venus_surface.jpg')
earth = Entity(model='sphere',  scale=0.8, texture = "textures/earth albedo.jpg")
mars = Entity(model='obj/Mars 2K.obj', scale=0.2, texture = 'textures/mars.png')
jupiter = Entity(model='sphere',scale=1.2, texture = 'textures/jupitermap.jpg')
saturn = Entity(model= 'sphere', scale=1, texture = 'textures/saturnmap.jpg')
uranus = Entity(model='sphere', scale=1, texture = 'textures/uranusmap.jpg')
neptune = Entity(model='sphere',  scale=1, texture = 'textures/neptunemap.jpg')
pluto = Entity(model='sphere', scale=0.4, texture = 'plutomap1k.jpg')

t = -math.pi

app.run()
