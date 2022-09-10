# 프로그래머스 주차요금정산
# https://school.programmers.co.kr/learn/courses/30/lessons/92341

def solution(fees, records):
    answer = []
    inout_dict = dict()
    
    for record in records:
        time, car_num, order = record.split()
        if car_num not in inout_dict:
            inout_dict[car_num] = [time]
        else:
            inout_dict[car_num].append(time)
    
    for key, value in inout_dict.items():
        if len(value) % 2:
            inout_dict[key].append('23:59')

    for _, value in sorted(inout_dict.items()):
        parked_time = 0
        for i, time in enumerate(value[::2]):
            out_h, out_m = list(map(int, value[i * 2 + 1].split(':')))
            in_h, in_m = list(map(int, value[i * 2].split(':')))
            parked_time += (out_h - in_h) * 60 + (out_m - in_m)
        
        temp_fee = fees[1]
        parked_time -= fees[0]
        if parked_time > 0:
            if parked_time % fees[2]:
                temp_fee += (parked_time // fees[2] + 1) * fees[3]
            else:
                temp_fee += (parked_time // fees[2]) * fees[3]
        answer.append(temp_fee)
    
    return answer