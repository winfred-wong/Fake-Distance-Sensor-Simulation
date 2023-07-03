import matplotlib.pyplot as plt
from FakeDistanceSensorSimulation.config import *
import numpy as np


class MapManager:

    def __init__(self, update_delay=0.0001):
        self.update_delay = update_delay
        self.x = []
        self.y = []
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.sc = self.ax.scatter(self.x, self.y)
        plt.xlim(0, world_width * 1.1)
        plt.ylim(0, world_height * 1.1)
        plt.draw()

    def update_plot(self, new_x, new_y):
        self.x.append(new_x)
        self.y.append(new_y)
        self.sc.set_offsets(np.c_[self.x, self.y])
        self.fig.canvas.draw_idle()
        plt.pause(self.update_delay)
