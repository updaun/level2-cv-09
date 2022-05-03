# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    news = ''
    for ss in s:
        if ss in "{}":
            pass
        else:
            news += ss
    tup = news.split(',')
    counter = {}
    for n in tup:
        if n in counter:
            counter[n] += 1
        else:
            counter[n] = 1
    sort = sorted(counter.items(),
                  key = lambda item: item[1],
                  reverse=True)
    for i in sort:
        answer.append(int(i[0]))
    return answer