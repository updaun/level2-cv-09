# kakao 2019 blind
# open chatting room
# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    nick_name_dict = dict()
    result_list = list()
    
    for line in record:
        token = line.split()
        temp = ""
        if token[0] == "Enter":
            nick_name_dict[token[1]] = token[2]
            temp = "Enter " + token[1]
        if token[0] == "Change":
            nick_name_dict[token[1]] = token[2]
        if token[0] == "Leave":
            temp = "Leave " + token[1]
        if temp:
            result_list.append(temp)
    
    for result in result_list:
        order, uid = result.split()
        temp = ""
        if order == "Enter":
            temp = nick_name_dict[uid] + "님이 들어왔습니다."
        if order == "Leave":
            temp = nick_name_dict[uid] + "님이 나갔습니다."
        answer.append(temp)
    
    return answer