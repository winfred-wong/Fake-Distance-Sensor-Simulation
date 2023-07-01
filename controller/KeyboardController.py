import numpy as np


class KeyboardController:
    def __init__(self, world):
        self._steering = 0.
        self._throttle = 0.

        self.min_steering = -0.5
        self.max_steering = +0.5

        self.min_throttle = -1.5
        self.max_throttle = +1.5

        world.visualizer.win.bind("<KeyRelease-Up>", self.arrow_up_release)
        world.visualizer.win.bind("<KeyRelease-Down>", self.arrow_down_release)
        world.visualizer.win.bind("<KeyRelease-Left>", self.arrow_left_release)
        world.visualizer.win.bind("<KeyRelease-Right>", self.arrow_right_release)

        world.visualizer.win.bind("<KeyPress-Up>", self.arrow_up_press)
        world.visualizer.win.bind("<KeyPress-Down>", self.arrow_down_press)
        world.visualizer.win.bind("<KeyPress-Left>", self.arrow_left_press)
        world.visualizer.win.bind("<KeyPress-Right>", self.arrow_right_press)

        world.visualizer.win.focus_force()  # very impolite... Polite version is focus_set(), but it is not always working

    @property
    def steering(self):
        return self._steering

    @property
    def throttle(self):
        return self._throttle

    @steering.setter
    def steering(self, val):
        self._steering = np.clip(val, self.min_steering, self.max_steering)

    @throttle.setter
    def throttle(self, val):
        self._throttle = np.clip(val, self.min_throttle, self.max_throttle)

    def arrow_up_release(self, event):
        self.throttle -= 1.5

    def arrow_down_release(self, event):
        self.throttle += 1.5

    def arrow_left_release(self, event):
        self.steering -= 0.5

    def arrow_right_release(self, event):
        self.steering += 0.5

    def arrow_up_press(self, event):
        self.throttle += 1.5

    def arrow_down_press(self, event):
        self.throttle -= 1.5

    def arrow_left_press(self, event):
        self.steering += 0.5

    def arrow_right_press(self, event):
        self.steering -= 0.5
