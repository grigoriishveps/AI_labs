
def start_dfs(start, answer, with_pause):
    f = open('log.txt', 'w')
    history = [(start,"start")]
    print(start)
    dfs_two(start, answer, history, with_pause)
    print("Длина истории" ,len(history))
    for i in range(len(history)):
        f.write(str(i) + '\n')
        f.write(str(history[i][0]) + '\n')
        f.write("done - " + str(history[i][1]) + '\n')
    x = 0
    while(x!=-1):
        print(history[x][0])
        print("done - ", history[x][1])
        x = int(input())
    print("Конец просмотра")

def dfs_two(state, answer, history, with_pause):
    stack = [[state, 0, 0]]
    while len(stack)!=0:
        state = stack[-1][0]
        done = stack[-1][1]
        pred = stack[-1][2]

        if state==answer:
            history.append((state, "end"))
            return True
        # проверка повтора узла
        for i in range(len(stack)-2, -1,-1):
            if stack[i][0] == state:
                history.append((state, "repeat"))
                stack.pop()
                break
        else:
            # Выбор следующего узла
            if pred != 3 and done == 0 and state.has_right():
                new_state = state.move_right()
                history.append((new_state, "right"))
                stack[-1][1]= 1
                stack.append([new_state, 0, 1])
            elif pred != 4 and done <= 1 and state.has_down():
                new_state = state.move_down()
                history.append((new_state, "down"))
                stack[-1][1]= 2
                stack.append([new_state, 0, 2])
            elif pred != 1 and done <= 2 and state.has_left():
                new_state = state.move_left()
                history.append((new_state, "left"))
                stack[-1][1]= 3
                stack.append([new_state, 0, 3])
            elif pred != 2 and done <= 3 and state.has_up():
                new_state = state.move_up()
                history.append((new_state, "up"))
                stack[-1][1] = 4
                stack.append([new_state, 0, 4])
            else:
                stack.pop()
                history.append((state, "block -1"))


