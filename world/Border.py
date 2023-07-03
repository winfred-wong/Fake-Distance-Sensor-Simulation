from FakeDistanceSensorSimulation.fake_sensor.FakeDistanceSensor import FakeDistanceSensor
from FakeDistanceSensorSimulation.world.entities import RectangleEntity
from FakeDistanceSensorSimulation.physics.geometry import Point


class Border(RectangleEntity):
    def __init__(self, center: Point, size: Point, heading: float, color: str = 'green'):
        movable = False
        friction = 0.
        super(Border, self).__init__(center, heading, size, movable, friction)
        self.color = color
        self.collidable = True
