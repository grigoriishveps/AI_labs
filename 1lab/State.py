import numpy as np


class TurnException(Exception):
    def __init__(self, turn_name: str):
        super()
        self.turn_name = turn_name

    def __str__(self):
        return "Unable to move " + self.turn_name


def check_turn(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is None:
            raise TurnException(func.__name__.split("_")[1])
        else:
            return result

    return wrapper


class State:
    def __init__(self, array: np.ndarray):
        self.grid = np.copy(array)
        coord = np.where(array == 0)
        self.x = coord[0][0]
        self.y = coord[1][0]
        self.final = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    def has_left(self):
        return self.y != 0

    def has_right(self):
        return self.y != 2

    def has_up(self):
        return self.x != 0

    def has_down(self):
        return self.x != 2

    @check_turn
    def move_left(self):
        if self.has_left():
            new_grid = self.grid.copy()
            x = self.x
            y = self.y
            new_grid[x][y], new_grid[x][y - 1] = new_grid[x][y - 1], new_grid[x][y]
            return State(new_grid)

    @check_turn
    def move_right(self):
        if self.has_right():
            new_grid = self.grid.copy()
            x = self.x
            y = self.y
            new_grid[x][y], new_grid[x][y + 1] = new_grid[x][y + 1], new_grid[x][y]
            return State(new_grid)

    @check_turn
    def move_up(self):
        if self.has_up():
            new_grid = self.grid.copy()
            x = self.x
            y = self.y
            new_grid[x][y], new_grid[x - 1][y] = new_grid[x - 1][y], new_grid[x][y]
            return State(new_grid)

    @check_turn
    def move_down(self):
        if self.has_down():
            new_grid = self.grid.copy()
            x = self.x
            y = self.y
            new_grid[x][y], new_grid[x + 1][y] = new_grid[x + 1][y], new_grid[x][y]
            return State(new_grid)

    def is_final(self):
        return np.array_equal(self.grid, self.final)

    def __str__(self):
        return str(self.grid)
