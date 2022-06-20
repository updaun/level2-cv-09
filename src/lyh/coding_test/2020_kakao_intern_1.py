# 프로그래머스, 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256

def distance(coord_1, coord_2):
    return abs(coord_1[0]-coord_2[0]) + abs(coord_1[1]-coord_2[1])

def solution(numbers, hand):
    answer = ''
    num_coord = {
        '1' : [0, 3], '2' : [1, 3], '3' : [2, 3],
        '4' : [0, 2], '5' : [1, 2], '6' : [2, 2],
        '7' : [0, 1], '8' : [1, 1], '9' : [2, 1],
        '*' : [0, 0], '0' : [1, 0], '#' : [2, 0]
    }
    left_pos, right_pos = '*', "#"
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left_pos = str(num)
        elif num in [3, 6, 9]:
            answer += 'R'
            right_pos = str(num)
        else:
            left_dis = distance(num_coord[left_pos], num_coord[str(num)])
            right_dis = distance(num_coord[right_pos], num_coord[str(num)])
            if left_dis < right_dis:
                answer += 'L'
                left_pos = str(num)
            elif left_dis > right_dis:
                answer += 'R'
                right_pos = str(num)
            else:
                if hand == 'left':
                    answer += 'L'
                    left_pos = str(num)
                else:
                    answer += 'R'
                    right_pos = str(num)
        
    return answer