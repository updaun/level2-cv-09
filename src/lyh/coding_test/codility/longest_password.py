# codility easy task
# https://app.codility.com/c/run/trainingQ5MHK6-AVX/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def check_validation(word):
    alpha_cnt, digit_cnt = 0, 0
    for char in word:
        if char.isalpha():
            alpha_cnt += 1
        elif char.isdigit():
            digit_cnt += 1
        else:
            return False
    if (not (alpha_cnt % 2)) and (digit_cnt % 2):
        return True
    return False

def solution(S):
    # write your code in Python 3.8.10
    # check a-z, A-Z, 0-9
    # even letters, odd digits
    word_list = S.strip().split()
    longest_word = -1

    for word in word_list:
        if check_validation(word):
            longest_word = max(longest_word, len(word))
    
    return longest_word