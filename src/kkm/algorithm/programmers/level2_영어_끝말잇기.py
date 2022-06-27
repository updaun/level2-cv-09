# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = []
    
    repeat = [words[0]]
    i = 1
    turn = 2
    while True:
        if i == len(words): return [0,0]
        if words[i] in repeat:
            print(turn)
            return [turn, i // n + 1]
        if words[i][0] != words[i-1][-1]:
            return [turn, i // n + 1]
        repeat.append(words[i])
        i += 1
        turn += 1
        if turn > n:
            turn = 1
    return answer