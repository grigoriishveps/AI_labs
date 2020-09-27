import numpy as np
from State import State

if __name__ == '__main__':
    print("ready")
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
    # a = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
    # a = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
    # a = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
    a_result = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    state = State(a)
    print(a)

    print("has", state.has_down())
    state.move_left().print_state()
    state.move_left().move_left().print_state()
    #print_state("Answer", a)
    print("Answer\n", np.where(a_result==0))

    #print_state(a)
