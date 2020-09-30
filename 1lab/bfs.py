from State import State
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue
import time
q = Queue()
done = False
final_state = State(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))
state_hist = list()


def blind_search_bfs():
    with ThreadPoolExecutor() as executor:
        global done
        global q
        while not done:
            executor.submit(thread_func).add_done_callback(work_done)
            # if queue.qsize() % 1000 == 0:
            print("Stack")
            print(q.qsize())
            # if len(state_hist) % 1000 == 0:
            #     print("State hist")
            #     print(len(state_hist))


def work_done(future):
    t = future.result()
    if t is not None:
        global done
        done = True
        print(t)


def thread_func():
    global q
    state = q.get()
    if state == final_state:
        global done
        if not done:
            return state
    else:
        global state_hist
        if state in state_hist:
            return
        else:
            state_hist.append(state)
        if state.has_up():
            q.put(state.move_up())
            # print("Empty moved up")
            # print(stack[-1])
        if state.has_down():
            q.put(state.move_down())
            # print("Empty moved down")
            # print(stack[-1])
        if state.has_left():
            q.put(state.move_left())
            # print("Empty moved left")
            # print(stack[-1])
        if state.has_right():
            q.put(state.move_right())
            # print("Empty moved right")
            # print(stack[-1])


if __name__ == '__main__':
    time1 = time.perf_counter()
    q.put(State(np.array([[1, 2, 3], [4, 5, 0], [6, 7, 8]])))
    blind_search_bfs()
    time2 = time.perf_counter()
    print(time2 - time1)
