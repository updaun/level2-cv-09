# backjoon 2580, sudoku
# 	138600kb	2772ms

import sys
graph = []
blank = []

'''
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
'''

def sudoku():
    fill_graph()
    fill_blank()
    dfs(0)

def fill_graph():
    for _ in range(9):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

def fill_blank():
    for i, line in enumerate(graph):
        for j, num in enumerate(line):
            if not num:
                blank.append((i, j))

def possible(x, y, num):
    for i in range(9):
        if graph[x][i] == num:
            return False

    for i in range(9):
        if graph[i][y] == num:
            return False

    for i in range(x//3*3, x//3*3+3):
        for j in range(y//3*3, y//3*3+3):
            if graph[i][j] == num:
                return False
    return True

def print_graph():
    for i in range(9):
        print(*graph[i])

def dfs(n):
    if n == len(blank):
        print_graph()
        exit(0)

    for num in range(1, 9 + 1):
        x, y = blank[n]
        if possible(x, y, num):
            graph[x][y] = num
            dfs(n+1)
            graph[x][y] = 0

sudoku()