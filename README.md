# Fake Distance Sensor Simulation For SLAM

A fake distance sensor simulation powered by CARLO. This repo contains a fake sensor class that can simulate a real
world distance sensor and output distance data as the car moves around in the simulated world. Additionally, a mapping
functionality is added, so that we can visualise the fake distance sensor's data to simulate mapping as the car move
around. Video is attached below for reference.

## Video

![](https://j.gifs.com/pZDnop.gif)

## Installation

As said, this repo is highly dependent on CARLO, please follow the instructions on CARLO's repo.
[CARLO](https://github.com/Stanford-ILIAD/CARLO/tree/allan)
No other additional installation is required except those stated in CARLO.

## Running

Simply run

```
    python example.py
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

Based on [Do Lines intersect?](https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/), we can find
out if two lines
segments intersect. Then,
using [Fine intersection of two lines](https://www.cuemath.com/geometry/intersection-of-two-lines/) we can find the
intersection point
of two lines. From here, we have the heading angle of the car and the coordinate (with respect to the car) of the wall.
So we convert the coordinate to that with respect to the origin by addition and then calculate the distance between
the car and the coordinate of the wall with respect to the origin to simulate a distance sensor. Finally, with the
heading angle
and distance, we can convert from polar coordinate to cartesian to draw a dot on the map and as the car moves, we will
complete the map.

## GeoGebra

There is a .ggb file, which helps you understand and visualise the parameters used in this project. You can navigate to
[GeoGebra](https://www.geogebra.org/calculator) to open the file and have a look to test out with different settings.