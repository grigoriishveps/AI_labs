import numpy as np
from State import State

if __name__ == '__main__':
    print("ready")
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
    # a = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
    # a = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
    # a = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
    state: State = State(a)
    print("Initial State: ")
    print(a)
    print(state.x, state.y)
    print("Up:")
    new_state = state.move_up()
    print(new_state)
    print("Down:")
    new_state = new_state.move_down()
    print(new_state)
    print("Right:")
    print(new_state.move_right())
    print("Left:")
    print(new_state.move_left())
    #print_state("Answer", a)

    #print_state(a)

