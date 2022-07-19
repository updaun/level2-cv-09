import sys
for line in sys.stdin:
    s_count = [0,0,0,0]
    for s in line[:-1]:
        if s.islower():
            s_count[0] +=1
        elif s.isupper():
            s_count[1] +=1
        elif s.isdigit():
            s_count[2] +=1
        elif s.isspace():
            s_count[3] +=1
    print(" ".join(map(str, s_count)))