# solve x, y point of rectangle

def solution(v):
    answer = []
    
    v.sort(key=lambda x:x[0])
    temp = 0
    for i, x in enumerate(v):
        temp += x[0]*(-1)**i
    answer.append(abs(temp))

    v.sort(key=lambda x:x[1])
    temp = 0
    for i, y in enumerate(v):
        temp += y[1]*(-1)**i
    answer.append(abs(temp))

    return answer