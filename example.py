import numpy as np
from FakeDistanceSensorSimulation.config import *
from FakeDistanceSensorSimulation.config import world_width
from FakeDistanceSensorSimulation.world.Border import Border
from FakeDistanceSensorSimulation.world.Car import Car
from FakeDistanceSensorSimulation.physics.geometry import Point, Line
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

# The factor used to draw the border that resembles the border line used to draw the line in fake distance sensor is different
# This is for it to visualise the border line more accurately
close_side_border_visual_factor = close_side_border_factor - 0.053
height_compensation_factor = 1.55
i = 0

while i < 4:

    short_width = world_width * close_side_border_visual_factor
    long_width = world_width - short_width
    short_height = world_height * close_side_border_visual_factor * (height_compensation_factor if i < 2 else 1)
    long_height = world_height - short_height

    if i < 2:
        # Bottom > top
        border_line = Border(Point(world_width / 2, short_height if i == 0 else long_height),
                             Point(long_width, thickness_of_border), 0)
    else:
        # left > right
        border_line = Border(Point(short_width if i == 2 else long_width, world_height / 2),
                             Point(thickness_of_border, long_height), 0)
    w.add(border_line)
    i += 1

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
