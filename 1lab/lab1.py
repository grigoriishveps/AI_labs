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

    y = input("Для пошагового алгоритма введите - 1, иначе 0: ") == "1"
    x = input("Для поиска в ширину введите - bfs, а для поиска в длину - dfs: ")

    if x == "bfs":
        print("Здесь должен быть bfs", y)
    elif x == "dfs":
        start_dfs(State(a), State(res), y)
    else:
        print("Нет такого алгоритма")

    #print_state(a)

