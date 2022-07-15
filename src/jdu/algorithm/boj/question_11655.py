import sys
crypto = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i, k in enumerate(alphabet):
    temp = (i+13)%len(alphabet)
    crypto[k] = alphabet[temp]
input_str = sys.stdin.readline().rstrip()
result = ''
for s in input_str:
    if s.lower() in crypto.keys():
        if s.isupper():
            result += crypto[s.lower()].upper()
        else:
            result += crypto[s]
    else:
        result += s
print(result)