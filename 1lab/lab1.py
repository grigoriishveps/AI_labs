import numpy as np
from State import State
from dfs import start_dfs

if __name__ == '__main__':
    print("ready")
    # a = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
    #a = np.array([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
    #a = np.array([[1, 2, 3], [0, 4, 5], [7, 8, 6]])
    #light example
    #a = np.array([[1, 2, 3], [4, 0, 6], [7, 5, 8]])
    #common example
    #a = np.array([[1, 2, 3], [6, 0, 8], [7, 5, 4]])
    #hard example
    a = np.array([[5, 8, 1], [0, 7, 2], [3, 6, 4]])
    res = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    state: State = State(a)

    # print("Initial State: ")
    # print(a)
    # print(state.x, state.y)
    # print("Up:")
    # new_state = state.move_up()
    # print(new_state)
    # print("Down:")
    # new_state = new_state.move_down()
    # print(new_state)
    # print("Right:")
    # print(new_state.move_right())
    # print("Left:")
    # print(new_state.move_left())
    # print("Answer:")
    # print(new_state.move_right().is_final())

    #print_state("Answer", a)

    start_dfs(State(a), State(res))
    #print_state(a)

