import math


def pol2cart(radius, theta):
    theta = theta * math.pi / 180.0
    return radius * math.cos(theta), radius * math.sin(theta)
