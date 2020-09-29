from typing import List
from State import State
import numpy as np
import os

global_states = list()

i = 0


def blind_search_bfs(stack: List[State]):
    final_state = State(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))
    state_hist = list()
    i = 0
    while len(stack) != 0:
        i += 1
        state = stack.pop(0)
        if state == final_state:
            print("Iterations: ", i)
            return state
        else:
            if state in state_hist:
                continue
            else:
                state_hist.append(state)
            if state.has_up():
                stack.append(state.move_up())
                # print("Empty moved up")
                # print(stack[-1])
            if state.has_down():
                stack.append(state.move_down())
                # print("Empty moved down")
                # print(stack[-1])
            if state.has_left():
                stack.append(state.move_left())
                # print("Empty moved left")
                # print(stack[-1])
            if state.has_right():
                stack.append(state.move_right())
                # print("Empty moved right")
                # print(stack[-1])
        if len(stack) % 1000 == 0:
            print("Stack")
            print(len(stack))
        if len(state_hist) % 1000 == 0:
            print("State hist")
            print(len(state_hist))


if __name__ == '__main__':
    res = blind_search_bfs([State(np.array([[5, 8, 3], [4, 0, 2], [7, 6, 1]]))])
    print(res)
