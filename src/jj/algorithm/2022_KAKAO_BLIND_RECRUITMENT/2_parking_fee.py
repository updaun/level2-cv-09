# source: https://programmers.co.kr/learn/courses/30/lessons/92341

'''
주어지는 것: 주차장 요금표, 입차/출차 기록
차량별로 주차 요금 계산

입차 후 출차 내역 없다면, 23:59에 출차된 것으로 간주.
00:00부터 23:59 까지의 입/출차 내역을 바탕으로 차량별 누적 주차 시간을 계산하여 요금을 일괄로 정산.

누적 주차 시간 기본 시간 초과 시, 기본 요금에 더해서 초과한 시간에 대해서 단위 시간 마다 단위 요금 청구.
'''

'''
fees: 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
records: "시각 차량번호 내역"
'''

# 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return

def solution(fees, records):
    
    car_number = list(set([x.split(' ')[1] for x in records]))
    
    park_time = dict()
    
    for num in car_number:
        park_time[num] = []
    
    for record in records:
        time, num, _ = record.split(' ')
        
        hour, minute = time.split(':')
        
        time = int(hour) * 60 + int(minute)
        
        park_time[num].append(time)
    
    for num, time in list(park_time.items()):
        
        total_park_time = 0
        
        if len(time) % 2 == 0:
            for i in range(0, len(time), 2):
                total_park_time += time[i+1] - time[i]
            
        # 마지막 출차 기록이 없는 경우
        else:
            for i in range(0, len(time)-1, 2):
                total_park_time += time[i+1] - time[i]
            
            total_park_time += 23*60 + 59 - time[-1]
        
        # fees: 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
        if total_park_time <= fees[0]:
            fee = fees[1]
        else:
            if (total_park_time - fees[0]) % fees[2]:
                fee = fees[1] + ((total_park_time - fees[0]) // fees[2] + 1) * fees[3]
            else:
                fee = fees[1] + (total_park_time - fees[0]) // fees[2] * fees[3]
            
        park_time[num] = fee
    
    park_fee = list(park_time.items())
    park_fee = sorted(park_fee, key=lambda x : x[0])
    
    answer = [x[1] for x in park_fee]
    
    return answer