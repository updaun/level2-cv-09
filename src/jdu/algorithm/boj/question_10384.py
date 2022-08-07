import sys
input = sys.stdin.readline
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(1, int(input())+1):
    alpha_dict = dict()
    for s in alphabet:
        alpha_dict[s] = 0
    for s in input().rstrip():
        if s.isalpha():
            alpha_dict[s.lower()] += 1
    if min(alpha_dict.values()) == 0:
        print(f"Case {i}: Not a pangram")
    else:
        if 1 in alpha_dict.values():
            print(f"Case {i}: Pangram!")
        elif 1 not in alpha_dict.values() and 2 in alpha_dict.values():
            print(f"Case {i}: Double pangram!!")
        else:
            print(f"Case {i}: Triple pangram!!!")