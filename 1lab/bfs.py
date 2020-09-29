from typing import List
from State import State
import numpy as np

global_states = list()

final_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])


def blind_search_bfs(stack: List[State]):
    state = stack.pop(0)
    if state == final_state:
        return state
    else:
        if state.has_up():
            stack.append(state.move_up)
            print("Empty moved up")
            print(stack[-1])
            blind_search_bfs(stack)
        if state.has_down():
            stack.append(state.move_down)
            print("Empty moved down")
            print(stack[-1])
            blind_search_bfs(stack)
        if state.has_left():
            stack.append(state.move_left)
            print("Empty moved left")
            print(stack[-1])
            blind_search_bfs(stack)
        if state.has_right():
            stack.append(state.move_right)
            print("Empty moved right")
            print(stack[-1])
            blind_search_bfs(stack)


if __name__ == '__main__':
    blind_search_bfs([State(np.array([[5, 8, 3], [4, 0, 2], [7, 6, 1]]))])
