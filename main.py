from turtle import position
from ursina import *
import math

def update():
    global t
    t = t + 0.0002
    angle = math.pi*40/180
    mercury_factor=365/88
    venus_factor=365/225
    earth_factor=365/365
    mars_factor=365/687
    jupiter_factor=365/4333
    saturn_factor=365/10759
    uranus_factor=365/30687
    neptune_factor=365/10690
    pluto_factor=365/90520
    
    #rotate around the sun
    # radius variable is the distance between the planet and the sun
    # the angle variable is the angle matched by the sun on the Oxygen plane
    # there are 9 planets in all around the sun so 360/9 = 40, each planet is 40 degrees apart, angle has radians
    # variable t is a time variable, i.e. when taking cos, sine of t, each frame of planets will change positions according to the coordinates calculated in t
    # this planet I give distance for being lazy
    
    radius_1 = 5.22
    mercury.x = math.cos(mercury_factor*t)*radius_1
    mercury.z = math.sin(mercury_factor*t)*radius_1
    
    radius_2 = 10.81
    venus.x = math.cos(venus_factor*t+angle)*radius_2
    venus.z = math.sin(venus_factor*t+angle)*radius_2

    radius_3 = 14.72
    earth.x = math.cos(earth_factor*t+angle*2)*radius_3
    earth.z = math.sin(earth_factor*t+angle*2)*radius_3

    radius_4 = 21.78
    mars.x = math.cos(mars_factor*t+angle*3)*radius_4
    mars.z = math.sin(mars_factor*t+angle*3)*radius_4

    radius_5 = 77.07
    jupiter.x = math.cos(jupiter_factor*t+angle*4)*radius_5
    jupiter.z = math.sin(jupiter_factor*t+angle*4)*radius_5

    radius_6 = 142.7
    saturn.x = math.cos(saturn_factor*t+angle*5)*radius_6
    saturn.z = math.sin(saturn_factor*t+angle*5)*radius_6

    radius_7 = 275.2
    uranus.x = math.cos(uranus_factor**t+angle*6)*radius_7
    uranus.z = math.sin(uranus_factor*t+angle*6)*radius_7

    radius_8 = 452.9
    neptune.x = math.cos(neptune_factor*t+angle*7)*radius_8
    neptune.z = math.sin(neptune_factor*t+angle*7)*radius_8

    radius_9 = 590
    pluto.x = math.cos(pluto_factor*t+angle*8)*radius_9
    pluto.z = math.sin(pluto_factor*t+angle*8)*radius_9

    #tự xoay quanh trục 
    sun.rotation_y += time.dt*5
    mercury.rotation_y += time.dt*10
    earth.rotation_y += time.dt*-10
    venus.rotation_y += time.dt*10
    mars.rotation_y += time.dt*10
    jupiter.rotation_y += time.dt*10
    saturn.rotation_y += time.dt*10
    uranus.rotation_y += time.dt*10
    neptune.rotation_y += time.dt*10
    pluto.rotation_y += time.dt*10

class Sky(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = 'textures/StarsMap_2500x1250.jpg',
            parent = scene,
            scale = 2000,
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
