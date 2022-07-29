import sys
input = sys.stdin.readline
def str2dict(input_str):
    output_dict = {}
    for s in input_str:
        if s not in output_dict.keys():
            output_dict[s] = 1
        else:
            output_dict[s] += 1
    return output_dict
order = 1
while True:
    input_word = input().rstrip()
    check_word = input().rstrip()
    if input_word == 'END' and check_word == 'END':
        break
    input_dict = str2dict(input_word)
    check_dict = str2dict(check_word)
    if input_dict == check_dict:
        print(f'Case {order}: same')
    else:
        print(f'Case {order}: different')
    order += 1