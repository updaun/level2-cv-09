def solution(board, moves):
    tmp, answer = [], 0

    while len(moves):
        for i in range(len(board)):
            if board[i][moves[0]-1] != 0: # 인형이 있는 경우
                tmp.append(board[i][moves[0]-1])
                board[i][moves[0]-1] = 0
                moves.remove(moves[0])
                break
            elif i == len(board)-1:
                moves.remove(moves[0]) # 인형이 없는 경우

    if tmp == []: return 0
    while True:
        before = answer
        for i, _ in enumerate(tmp[:len(tmp)-1]):
            if tmp[i] == tmp[i+1]:
                del tmp[i+1]
                del tmp[i]
                answer += 2
                break
        if before == answer:
            break #더 이상 터질게 없으면

    return answer