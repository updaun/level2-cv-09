# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = []
    dictionary = {}
    for string in strings:
        if string[n] in dictionary:
            dictionary[string[n]].append(string)
        else:
            dictionary[string[n]] = [string]
    for s in sorted(dictionary.items()):
        if len(s[1]) > 1:
            for s1 in sorted(s[1]):
                answer.append(s1)
        else:
            answer.append(s[1][0])
    return answer