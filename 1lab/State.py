import numpy as np


class State:
    def __init__(self, array):
        self.state = np.copy(array)
        coord = np.where(array == 0)
        self.x = coord[0][0]
        self.y = coord[1][0]

    def has_left(self):
        return self.y != 0

    def has_right(self):
        return self.y != 2

    def has_up(self):
        return self.x != 0

    def has_down(self):
        return self.x != 2

    def move_left(self):
        if (self.has_left()):
            new_state = np.copy(self.state)
            x = self.x;
            y = self.y;
            new_state[x][y],new_state[x][y-1] = new_state[x][y-1],new_state[x][y]
            return State(new_state);

    def print_state(self):
        print(self.state)