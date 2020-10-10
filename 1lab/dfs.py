def check_state(hsh_tbl, state):
    hsh = hash(state)
    if hsh_tbl.get(hsh) is None:
        hsh_tbl[hsh] = 5
        return False
    else:
        return True


def start_dfs(start, answer, with_pause):
    f = open('log.txt', 'w')
    history = [(start, "start")]
    if with_pause:
        dfs_with_pause(start, answer, history)

    else:
        dfs_without_pause(start, answer, history)
        print("Длина истории", len(history))
        for i in range(len(history)):
            f.write(str(i) + '\n')
            f.write(str(history[i][0]) + '\n')
            f.write("done - " + str(history[i][1]) + '\n')
        x = 0
        print("Режим просмотра истории, введите значение от 0 до ", len(history))
        while x != -1:
            print(history[x][0])
            print("done - ", history[x][1])
            x = int(input())
    print("Конец просмотра")


def dfs_without_pause(state, answer, history):
    stack = [[state, 0, 0]]
    hsh_tbl = {}
    while len(stack) != 0:
        state, done, pred = stack[-1]

        if state == answer:
            history.append((state, "end"))
            return True


        if done == 0 and check_state(hsh_tbl, state):
            history.append((state, "repeat"))
            stack.pop()
        else:
            # Выбор следующего узла
            if pred != 3 and done == 0 and state.has_right():
                new_state = state.move_right()
                history.append((new_state, "right"))
                stack[-1][1] = 1
                stack.append([new_state, 0, 1])
            elif pred != 4 and done <= 1 and state.has_down():
                new_state = state.move_down()
                history.append((new_state, "down"))
                stack[-1][1] = 2
                stack.append([new_state, 0, 2])
            elif pred != 1 and done <= 2 and state.has_left():
                new_state = state.move_left()
                history.append((new_state, "left"))
                stack[-1][1] = 3
                stack.append([new_state, 0, 3])
            elif pred != 2 and done <= 3 and state.has_up():
                new_state = state.move_up()
                history.append((new_state, "up"))
                stack[-1][1] = 4
                stack.append([new_state, 0, 4])
            else:
                stack.pop()
                history.append((state, "block -1"))


def dfs_with_pause(state, answer, history):
    stack = [[state, 0, 0]]
    hsh_tbl = {}
    print(
        "Для просмотра 5последних значений стека на каждом этапе алгоритма введите строку stack, иначе простот нажмите Enter")
    while len(stack) != 0:
        state = stack[-1][0]
        done = stack[-1][1]
        pred = stack[-1][2]

        print("Текущее обрабатываемое состояние")
        print(state)
        x = input()
        if (x == "stack"):
            print("Последние 5 значения стека")
            for i in range(len(stack) - 1, max(-1, len(stack) - 6), -1):
                print(stack[i][0])

        if state == answer:
            return True
        # проверка повтора узла
        if done == 0 and check_state(hsh_tbl, state):
            print("done - repeat")
            stack.pop()
        else:
            # Выбор следующего узла
            if pred != 3 and done == 0 and state.has_right():
                new_state = state.move_right()
                print("done - right\n")
                stack[-1][1] = 1
                stack.append([new_state, 0, 1])
            elif pred != 4 and done <= 1 and state.has_down():
                new_state = state.move_down()
                print("done - down\n")
                stack[-1][1] = 2
                stack.append([new_state, 0, 2])
            elif pred != 1 and done <= 2 and state.has_left():
                new_state = state.move_left()
                print("done - left\n")
                stack[-1][1] = 3
                stack.append([new_state, 0, 3])
            elif pred != 2 and done <= 3 and state.has_up():
                new_state = state.move_up()
                print("done - up\n")
                stack[-1][1] = 4
                stack.append([new_state, 0, 4])
            else:
                stack.pop()
                print("done - block -1\n")
