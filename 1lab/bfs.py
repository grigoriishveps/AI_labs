from typing import List
from State import State

global_states = list()


def blind_search_bfs(stack: List[State]):
    state = stack.pop(0)
    if state.is_final():
        return state
    else:
        if state.has_up():
            stack.append(state.move_up)
            blind_search_bfs(stack)
        if state.has_up():
            stack.append(state.move_up)
            blind_search_bfs(stack)
        if state.has_up():
            stack.append(state.move_up)
            blind_search_bfs(stack)
        if state.has_up():
            stack.append(state.move_up)
            blind_search_bfs(stack)
