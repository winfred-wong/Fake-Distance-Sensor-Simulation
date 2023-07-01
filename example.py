import numpy as np
from FakeDistanceSensorSimulation.config import *
from FakeDistanceSensorSimulation.config import world_width
from FakeDistanceSensorSimulation.world.Car import Car
from FakeDistanceSensorSimulation.physics.geometry import Point
import time
from FakeDistanceSensorSimulation.controller.KeyboardController import KeyboardController
from FakeDistanceSensorSimulation.world.world import World

# Create a world
w = World(dt, width=world_width, height=world_height, ppm=6)

# Create a car and set the velocity and max/min speed
c1 = Car(Point(world_width / 2, world_height / 2), np.pi / 2)
c1.max_speed = 30.0
c1.min_speed = -30.0
c1.velocity = Point(0, 0)
w.add(c1)

# Render the world
w.render()

# initial steering and throttle, both 0
c1.set_control(0., 0.)

# Setup controller of the keyboard
controller = KeyboardController(w)

# Keep looping
while True:
    # Set the control from the keyboard
    c1.set_control(controller.steering, controller.throttle)

    # Let the world run
    w.tick()

    # Render
    w.render()

    # Watch the world in 4x speed
    time.sleep(dt / 4)
