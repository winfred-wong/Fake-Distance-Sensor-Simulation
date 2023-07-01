# Fake Distance Sensor Simulation

A fake distance sensor simulation powered by CARLO. This repo contains a fake sensor class that can simulate a real
world distance sensor and output distance data as the car moves around in the simulated world.

## Installation

As said, this repo is highly dependent on CARLO, please follow the instructions on CARLO's repo.
[CARLO](https://github.com/Stanford-ILIAD/CARLO/tree/allan)
No other additional installation is required except those stated in CARLO.

## Running

Simply run

```python
    python
example.py
```

## Details

The fake distance sensor can let you keep getting distance data in a simulated 2D world, so that you can start your
project, which needs a distance sensor, without actually buying one. You can also change the size of the world freely in
the config.py file.

Simply create an object of the class FakeDistanceSensor, which takes two arguments, with one being the heading angle of
the simulated car and the position of the car.

```
        fake_sensor = FakeDistanceSensor(heading_in_angle=self.heading_in_angle, car_center=self.center)
        fake_sensor.get_sensor_value()
```

The class will assume there is an imaginary line extending from the car's position to somewhere very far away.

1. The imaginary line is at the same heading angle of the car
2. The imaginary line must be longer than the longest diagonal of the rectangle to avoid mistakes

`Based on https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/`

Depending on the angle, we will calculate the x and y of the imaginary line using trigonometry. Then we find if the
imaginary line has intersections with the walls on four sides.
When we find out which side of the wall the imaginary line intersects with, we can then calculate the distance between
the wall and the car at that exact heading angle, this gives us the fake distance sensor data we need.
