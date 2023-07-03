import logging
from FakeDistanceSensorSimulation.config import *
from FakeDistanceSensorSimulation.helper import pol2cart
from FakeDistanceSensorSimulation.physics.geometry import Line, Point


class FakeDistanceSensor:
    def __init__(self, heading_in_angle: int, car_center: Point):
        self.heading_in_angle = heading_in_angle
        self.car_center = car_center

    def _get_endpoints_of_imagined_line(self):

        # The imaginary line has to be longer than the longest line possible within the rectangle for it to intersect
        # all possible lines
        # 169 when 80 tall 40 wide
        imaginary_line_length = int(math.hypot(world_width, world_height) + world_height)
        logging.debug(f"Length of imaginary line: {imaginary_line_length}")
        logging.debug(f"Car's heading in angle: {self.heading_in_angle}")

        # Convert to cartesian coordinates
        imagined_x, imagined_y = pol2cart(imaginary_line_length, self.heading_in_angle)

        # Convert the imagined coordinates to that with respect to origin
        imagined_x += self.car_center.x
        imagined_y += self.car_center.y
        logging.debug(f"Calculated p2 x, y position of imagined line: {imagined_x}, {imagined_y}")

        # Return x and y
        return imagined_x, imagined_y

    def get_sensor_value(self):

        imagined_x, imagined_y = self._get_endpoints_of_imagined_line()

        # Draw a line between the car and the imagined point
        car_straight_line = Line(self.car_center, Point(imagined_x, imagined_y))
        logging.debug(f"Two points of the imagined straight line: {car_straight_line}")

        short_width = world_width * close_side_border_factor
        long_width = world_width - short_width
        short_height = world_height * close_side_border_factor
        long_height = world_height - short_height

        # Walls for the world
        bottom_line: Line = Line(Point(short_width, short_height), Point(long_width, short_height))
        left_line: Line = Line(Point(short_width, short_height), Point(short_width, long_height))
        right_line: Line = Line(Point(long_width, short_height), Point(long_width, long_height))
        top_line: Line = Line(Point(short_width, long_height), Point(long_width, long_height))

        for line in [bottom_line, left_line, right_line, top_line]:
            intersection_point = car_straight_line.get_intersection_point(line)

            # intersects_with makes sure the intersection point is in front of the car (meaning it's facing that direction)
            # intersection_point finds out the intersection point
            if car_straight_line.intersects_with(line) and intersection_point:
                logging.debug(f"Intersection point detected and its coordinates: {intersection_point}")
                distance = self.car_center.distanceTo(intersection_point)
                logging.debug(f"The distance from the car to the intersection point: {distance}")
                return distance
        return 0
