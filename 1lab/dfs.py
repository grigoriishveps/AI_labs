import numpy as np
from State import State

def start_dfs(start, answer):

    history = [(start,"start")]
    print(start)
    #dfs(start, answer, history)
    dfs_two(start, answer, history)
    print("Длина истории" ,len(history))


    x = 0
    while(x!=-1):
        print(history[x][0])
        print("done - ", history[x][1])
        x = int(input())
    print("Конец просмотра")

def dfs_two(state, answer, history):

    stack = [(state, 0)]

    while len(stack)!=0:
        state = stack[-1][0]
        done = stack[-1][1]
        #flag = False
        if len(stack) %1000==0:
            print(len(stack))
        for i in range(len(stack)-2, 0,-1):

            if stack[i][0] == state:
                history.append((state, "repeat"))
                stack.pop()
                break
        # if flag:
        #     continue
        else:
            if state==answer or len(history)==10001:
                history.append((state, "end"))

                return True
            else:
                if done == 0 and state.has_right():
                    new_state = state.move_right()
                    history.append((new_state, "right"))
                    stack.pop()
                    stack.append((state, 1))
                    stack.append((new_state, 0))
                elif done <= 1 and state.has_down():
                    new_state = state.move_down()
                    history.append((new_state, "down"))
                    stack.pop()
                    stack.append((state, 2))
                    stack.append((new_state, 0))
                elif done <= 2 and state.has_left():
                    new_state = state.move_left()
                    history.append((new_state, "left"))
                    stack.pop()
                    stack.append((state, 3))
                    stack.append((new_state, 0))
                elif done <= 3 and state.has_up():
                    new_state = state.move_up()
                    history.append((new_state, "up"))
                    stack.pop()
                    stack.append((state, 4))
                    stack.append((new_state, 0))
                else:
                    stack.pop()
                    history.append((state, "block -1"))

                #print("Ошибка")
                #raise Exception("афваывываывпваьброд")




def dfs(state, answer, history):
    for i in range(len(history)-2, 0,-1):
        if history[i][1]=='start' or history[i][1]=="block -1":
            break
        elif history[i][0] == state:
            history.append((state, "repeat"))
            return False;
    if state==answer or len(history)==10001:
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
        return False
        #print("Ошибка")
        #raise Exception("афваывываывпваьброд")
