import time
from typing import List

import numpy as np

from State import State


def add_states_to_queue(state: State, queue: list):
    success = 0
    if state.has_up():
        queue.append(state.move_up())
        success += 1
    if state.has_down():
        queue.append(state.move_down())
        success += 1
    if state.has_left():
        queue.append(state.move_left())
        success += 1
    if state.has_right():
        queue.append(state.move_right())
        success += 1
    return success


def blind_search_bfs(queue: List[State], result: State, debug: bool = False):
    # init
    final_hash = hash(result)
    hsh_tbl = {}
    i = 0

    if debug:
        duplicate_vertices = list()

    while len(queue) != 0:
        state = queue.pop(0)
        hsh = hash(state)
        if hsh == final_hash:
            print("Iterations: ", i)
            return state
        else:
            if hsh_tbl.get(hsh) is None:
                hsh_tbl[hsh] = i
            else:
                if debug:
                    duplicate_vertices.append(state)
                continue

            success = add_states_to_queue(state, queue)
            i += 1

        if debug:
            print("--------------------------------------------------------------------------------------")
            print(f"Current state: \n {state}")
            print("Duplicated vertices added from last step:", *duplicate_vertices, sep='\n')
            duplicate_vertices.clear()
            print("Current state of queue first 2:", *queue[:2], "and last 2 objects:", *queue[-2:], sep='\n')
            print("Added to queue vertices on current step:", *queue[-success:], sep='\n')
            print("--------------------------------------------------------------------------------------")
            print("Press any key to move to next step")
            input()


if __name__ == '__main__':
    start = time.perf_counter()
    final_state = State(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))
    res = blind_search_bfs([State(np.array([[5, 8, 3], [4, 0, 2], [7, 6, 1]]))], final_state, debug=False)
    print(time.perf_counter() - start)
    print(res)
