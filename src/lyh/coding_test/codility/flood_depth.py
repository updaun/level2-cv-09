# codility medium task
# https://app.codility.com/c/run/trainingSMW85U-C4C/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.8.10
    if len(A) < 3:
        return 0
    
    stack = [[A[0], 0]]
    for height in A[1:]:
        # same height pass
        if height == stack[-1][0]:
            continue
        elif height < stack[-1][0]:
            # low height save
            stack.append([height, 0])
        else:
            # high height add
            max_depth = 0
            while len(stack) > 1 and height > stack[-1][0]:
                add_depth = min(stack[-2][0], height) - stack[-1][0]
                max_depth = max(max_depth, stack[-1][1]) + add_depth
                stack.pop()
            
            while len(stack) > 0 and height >= stack[-1][0]:
                max_depth = max(max_depth, stack[-1][1])
                stack.pop()
            stack.append([height, max_depth])
    
    answer = max(stack, key= lambda x : x[1])
    return answer[1]