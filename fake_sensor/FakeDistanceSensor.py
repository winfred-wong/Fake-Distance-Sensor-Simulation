import numpy as np
from FakeDistanceSensorSimulation.config import *
from FakeDistanceSensorSimulation.physics.geometry import Line, Point


class FakeDistanceSensor:
    def __init__(self, heading_in_angle: int, car_center: Point):
        self.heading_in_angle = heading_in_angle
        self.car_center = car_center

    def _get_angle_normalised_under_90(self):
        norm_angle = self.heading_in_angle
        while norm_angle >= 90:
            norm_angle -= 90
        return norm_angle

    def _get_quadrant(self):
        angle = self.heading_in_angle % 360

        if 0 <= angle < 90:
            return 1
        elif 90 <= angle < 180:
            return 2
        elif 180 <= angle < 270:
            return 3
        elif 270 <= angle < 360:
            return 4
        return None

    def _get_endpoints_of_imagined_line(self):
        # Normalise angle and get the quadrant
        angle = self._get_angle_normalised_under_90()
        quadrant = self._get_quadrant()

        # The imaginary line has to be longer than the longest line possible within the rectangle for it to intersect
        # all possible lines
        imaginary_line_length = int(math.hypot(world_width, world_height) + world_height)

        # a and b are new x and y of the imagined line depending on which quadrant they are in
        a = imaginary_line_length * np.sin(np.deg2rad(angle))
        b = imaginary_line_length * np.sin(np.deg2rad(90 - angle))

        # Assign the value depending on quadrant
        line_end_y = a if quadrant % 2 else b
        line_end_x = b if quadrant % 2 else a

        # Handle the negativity of the coordinate system
        if quadrant in [2, 3]:
            line_end_x *= -1

        if quadrant in [3, 4]:
            line_end_y *= -1

        return line_end_x, line_end_y

    def get_sensor_value(self):
        x, y = self._get_endpoints_of_imagined_line()

        # Draw a line between the car and the imagined point
        car_straight_line = Line(self.car_center, Point(x, y))

        short_width = world_width * close_side_border_factor
        long_width = world_width - short_width
        short_height = world_height * close_side_border_factor
        long_height = world_height - short_height

        # Walls for the world
        # Bottom > left > right > top
        for i, j in enumerate([[short_width, short_height, long_width, short_height],
                               [short_width, short_height, short_width, long_height],
                               [long_width, short_height, long_width, long_height],
                               [short_width, long_height, long_width, long_height]
                               ]):
            if i == 0:
                line_text = "bottom"
            elif i == 1:
                line_text = "left"
            elif i == 2:
                line_text = "right"
            else:
                line_text = "top"
            line: Line = Line(Point(j[0], j[1]), Point(j[2], j[3]))
            if car_straight_line.intersectsWith(line):
                print(f"Distance to {line_text} line: {self.car_center.distanceTo(line)}")
                return self.car_center.distanceTo(line)
            i += 1
