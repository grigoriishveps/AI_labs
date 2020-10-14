from sys import getsizeof
def check_state(hsh_tbl, state):
    hsh = hash(state)
    if hsh_tbl.get(hsh) is None:
        hsh_tbl[hsh] = 5
        return False
    else:
        return True

def state_list(stack ,is_last):
    result_arr = []
    for i in (stack[-3:] if is_last else stack[:3]):
        result_arr.append(i[0])
    return result_arr


def start_dfs(start, answer, with_pause):
    #выбор модификации алгоритма с паузами или без
    if with_pause:
        #Алгоритм с паузами
        dfs_with_pause(start, answer)
    else:
        #Алгоритм без пауз с автоматическим ведением истории пути алгоритма
        #c возможностью её просмотра в программе и выводом в файл
        f = open('log.txt', 'w')
        history = [(start, "start")]
        dfs_without_pause(start, answer, history)
        #Возможность просмотреть историю выбрав индекс итерации
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

# Поиск в глубину без паузами
def dfs_without_pause(state, answer, history):
    # стек для хранения пути поиска в глубину где значение элемента стека значит:
    # 0 - состояние - узел, 1 - какие пути пройдены от данного узла, 2 - из какого пути узел получен
    stack = [[state, 0, 0]]
    # хеш-таблица для быстрой проверки дубликатов
    hsh_tbl = {}
    #Начало циклического поиска в глубину
    while len(stack) != 0:

        state, done, pred = stack[-1]
        # сравнение текущего узла с финальным результатом
        if state == answer:
            history.append((state, "end"))
            return True
        # проверка узла на повторение если он был добавлен на прошлом шаге
        if done == 0 and check_state(hsh_tbl, state):
            history.append((state, "repeat"))
            stack.pop()
        else:
            # Выбор следующего узла проверяя какие узла уже были получены из данного состояния
            # и проверяя возможно ли получить эти узлы основываясь на границах поля
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

# Поиск в глубину с паузами
def dfs_with_pause(state, answer):
    # стек для хранения пути поиска в глубину где значение элемента стека значит:
    # 0 - состояние - узел, 1 - какие пути пройдены от данного узла, 2 - из какого пути узел получен
    stack = [[state, 0, 0]]
    #хеш-таблица для быстрой проверки дубликатов
    hsh_tbl = {}
    #массив для вывода информации о дубликате, обнаруженном на шаге
    duplicate_vertices = list()
    while len(stack) != 0:
        flag_pop = False
        state, done, pred = stack[-1]

        # сравнение текущего узла с финальным результатом
        if state == answer:
            return True
        # проверка узла на повторение если он был добавлен на прошлом шаге
        if done == 0 and check_state(hsh_tbl, state):
            duplicate_vertices.append(state)
            stack.pop()
        else:
            # Выбор следующего узла проверяя какие узла уже были получены из данного состояния
            # и проверяя возможно ли получить эти узлы основываясь на границах поля
            if pred != 3 and done == 0 and state.has_right():
                new_state = state.move_right()
                stack[-1][1] = 1
                stack.append([new_state, 0, 1])
            elif pred != 4 and done <= 1 and state.has_down():
                new_state = state.move_down()
                stack[-1][1] = 2
                stack.append([new_state, 0, 2])
            elif pred != 1 and done <= 2 and state.has_left():
                new_state = state.move_left()
                stack[-1][1] = 3
                stack.append([new_state, 0, 3])
            elif pred != 2 and done <= 3 and state.has_up():
                new_state = state.move_up()
                stack[-1][1] = 4
                stack.append([new_state, 0, 4])
            else:
                stack.pop()
                flag_pop = True

        print("--------------------------------------------------------------------------------------")
        print(f"Current state: \n {state}")
        print("Duplicated vertice from last step:", *duplicate_vertices, sep='\n')
        print("Current state of queue first 3:", *state_list(stack, False), "and last 3 objects:", *state_list(stack, True), sep='\n')
        if not (flag_pop):
            print("Added to queue vertice on current step:", stack[-1][0], sep='\n')
        else:
            print("On step vertice was delete from stack beacuse all direction was found or it was dublicate")
        print("--------------------------------------------------------------------------------------")
        print("Press any key to move to next step")
        input()
