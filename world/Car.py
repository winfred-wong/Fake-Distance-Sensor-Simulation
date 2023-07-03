from FakeDistanceSensorSimulation.fake_sensor.FakeDistanceSensor import FakeDistanceSensor
from FakeDistanceSensorSimulation.world.entities import RectangleEntity
from FakeDistanceSensorSimulation.physics.geometry import Point


class Car(RectangleEntity):
    def __init__(self, center: Point, heading: float, color: str = 'red'):
        size = Point(2., 1)
        movable = True
        friction = 0.06
        super(Car, self).__init__(center, heading, size, movable, friction)
        self.color = color
        self.collidable = True
        self.distanceToBorder = 0

    def tick(self, dt: float):
        # Execute global tick
        super(Car, self).tick(dt)
        fake_sensor = FakeDistanceSensor(heading_in_angle=self.heading_in_angle, car_center=self.center)
        self.distanceToBorder = fake_sensor.get_sensor_value()
