from typing import List
from State import State
import numpy as np
import time
import os

global_states = list()


def blind_search_bfs(stack: List[State]):
    final_state = State(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))
    state_hist = list()
    hsh_tbl = {}
    i = 0
    while len(stack) != 0:
        state = stack.pop(0)
        if state == final_state:
            print("Iterations: ", i)
            return state
        else:
            hsh = hash(state)
            if hsh_tbl.get(hsh) is None:
                hsh_tbl[hsh] = i
            else:
                continue
            if state.has_up():
                stack.append(state.move_up())
            if state.has_down():
                stack.append(state.move_down())
            if state.has_left():
                stack.append(state.move_left())
            if state.has_right():
                stack.append(state.move_right())
            i += 1


if __name__ == '__main__':
    start = time.perf_counter()
    res = blind_search_bfs([State(np.array([[5, 8, 3], [4, 0, 2], [7, 6, 1]]))])
    print(time.perf_counter() - start)
    print(res)
