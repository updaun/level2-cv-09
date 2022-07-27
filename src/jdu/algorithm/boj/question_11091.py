import sys
input = sys.stdin.readline
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(int(input())):
    alphabet_list = [i for i in alphabet]
    sentence = input().rstrip()
    for s in sentence:
        if s.lower() in alphabet_list:
            alphabet_list.remove(s.lower())
    if len(alphabet_list) == 0:
        print('pangram')
    else:
        missing = ''
        for s in alphabet_list:
            missing += s
        print(f'missing {missing}')