'''
define a "compressed word"
- a single, lower-case letter is a compressed word
- (e1 e2 ... et n), t, n: non-negative int & ei: compressed word

to uncompress the compressed word (e1 e2 ... et n),
uncompress each ei,
concatenate uncom words into a new word.
repeatedly concat that word n times.
'''

from collections import deque

w = input()

while w != '$':

    stack = deque([])
    w = deque(list(w))
    num = ''

    while w:
        c = w.popleft()

        if c == '(' or c.isalpha():
            stack.append(c)
        
        elif c.isdigit():
            num += c

        elif c == ')':
            num = int(num)

            stack2 = deque([])
            c = stack.pop()

            while c != '(':
                
                stack2.append(c)

                c = stack.pop()

            stack2 *= num

            num = ''
            
            while stack2:
                stack.append(stack2.pop())

    print(''.join(stack))

    w = input()