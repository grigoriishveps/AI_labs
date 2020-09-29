import numpy as np
from State import State
import sys
def start_dfs(start, answer):
    sys.setrecursionlimit(150000)
    history = [(start,"start")]
    print(start)
    dfs(start, answer, history)
    print("Длина истории" ,len(history))
    x = 0
    while(x!=-1):
        print(history[x][0])
        print("done - ", history[x][1])
        x = int(input())
    print("Конец просмотра")

def dfs(state, answer, history):
    for i in range(len(history)-2, 0,-1):
        if history[i][1]=='start' or history[i][1]=="block -1":
            break
        elif history[i][0] == state:
            history.append((state, "repeat"))
            return False;
    if state==answer or len(history)==100001:
        history.append((state, "end"))
        return True
    else:
        if state.has_right():
            history.append((state.move_right(), "right"))
            if dfs(state.move_right(), answer, history):
                return True
        if state.has_down():
            history.append((state.move_down(), "down"))
            if dfs(state.move_down(), answer, history):
                return True
        if state.has_left():
            history.append((state.move_left(), "left"))
            if dfs(state.move_left(), answer, history):
                return True
        if state.has_up():
            history.append((state.move_up(), "up"))
            if dfs(state.move_up(), answer, history):
                return True

        history.append((state, "block -1"))
        #print("Ошибка")
        #raise Exception("афваывываывпваьброд")
