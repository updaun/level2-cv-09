# https://programmers.co.kr/learn/courses/30/lessons/12901

import datetime

def solution(a, b):
    answer = ''
    
    days = ['MON','TUE','WED','THU','FRI','SAT', 'SUN']
    answer = days[datetime.datetime(2016, a, b).weekday()]    
    
    return answer