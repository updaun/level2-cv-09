# 프로그래머스
# 내 마음대로 string 정렬하기

def merge_sort(arr, n):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid], n)
    high_arr = merge_sort(arr[mid:], n)

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l][n] < high_arr[h][n]:
            merged_arr.append(low_arr[l])
            l += 1
        elif low_arr[l][n] == high_arr[h][n]:
            left_flag, right_flag = False, False
            for i in range(len(low_arr[l])):
                if low_arr[l][i] < high_arr[h][i]:
                    left_flag = True
                    break
                elif low_arr[l][i] > high_arr[h][i]:
                    right_flag = True
                    break
                if i == len(low_arr[l]) - 1:
                    if len(low_arr[l]) < len(high_arr[h]):
                        left_flag = True
                    elif len(low_arr[l]) > len(high_arr[h]):
                        right_flag = True
                    else:
                        left_flag = True
            if left_flag:
                merged_arr.append(low_arr[l])
                l += 1
            else:
                merged_arr.append(high_arr[h])
                h += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

def solution(strings, n):
    answer = []
    answer = merge_sort(strings, n)
    return answer