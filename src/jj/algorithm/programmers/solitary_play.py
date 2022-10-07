# source: https://school.programmers.co.kr/learn/courses/30/lessons/131130

'''
카드 100장 (1~100 번호)

2 이상 100 이하의 자연수를 정해 그 수보다 작거나 같은 숫자 카드들 준비.
카드를 상자에 한 장씩 넣고, 상자 무작위로 섞은 후 상자에 번호 기입.
임의의 상자 선택한 후, 상자 안의 카드 숫자 확인.
카드 숫자에 해당하는 상자 열기. 열어야 하는 상자가 이미 열려있을 때까지 반복.
이렇게 열린 상자들은 1번 상자 그룹.

1번 상자 그룹을 제외하고 남는 상자가 없으면 게임 종료. 0점 획득.
그렇지 않다면, 남은 상자 중 임의의 상자 골라 열려있는 상자를 만날 때까지 반복.
이렇게 열린 상자들은 2번 상자 그룹.

1번 상자 수 x 2번 상자 수가 점수.

최고 점수 return
'''
from collections import Counter

def solution(cards):
    
    cards = [0] + cards
    parent = [i for i in range(len(cards))]
    
    def find_parent(x):
        if parent[x] != x:
            return find_parent(parent[x])
        
        return x
    
    def union_parent(a, b):
        a = find_parent(a)
        b = find_parent(b)
        
        if a < b: parent[b] = a
        else: parent[a] = b
    
    
    for i in range(len(cards)):
        union_parent(i, cards[i])
        
    for i in range(len(cards)):
        parent[i] = find_parent(parent[i])
    
    parent = Counter(parent)
    
    score = parent.most_common()
    score = score[0][1] * score[1][1]
    
    if len(parent) == 2:
        return 0
    
    return score