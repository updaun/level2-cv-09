import sys
input = sys.stdin.readline
order = 1
while True:
    a, c, b = map(str, input().split())
    a = int(a)
    b = int(b)
    if c == 'E':
        break
    elif c == '>':
        print(f'Case {order}: {str(a > b).lower()}')
    elif c == '>=':
        print(f'Case {order}: {str(a >= b).lower()}')        
    elif c == '<':
        print(f'Case {order}: {str(a < b).lower()}')        
    elif c == '<=':
        print(f'Case {order}: {str(a <= b).lower()}')        
    elif c == '==':
        print(f'Case {order}: {str(a == b).lower()}')        
    elif c == '!=':
        print(f'Case {order}: {str(a != b).lower()}')
    order += 1
