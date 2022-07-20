def compare_elem(left_elem, right_elem):
    left_temp, right_temp = left_elem*3, right_elem*3
    return left_temp < right_temp
    
def merge(arr, left, mid, right):
    left_pos, right_pos = left, mid + 1
    sorted_list = list()

    while left_pos <= mid and right_pos <= right:
        if not compare_elem(str(arr[left_pos]), str(arr[right_pos])):
            sorted_list.append(arr[left_pos])
            left_pos += 1
        else:
            sorted_list.append(arr[right_pos])
            right_pos += 1
    
    if left_pos <= mid:
        sorted_list = sorted_list + arr[left_pos:mid+1]
    else:
        sorted_list = sorted_list + arr[right_pos:right+1]
    arr[left:right+1] = sorted_list

def merge_sort(arr, left, right):
    mid = (left + right) // 2
    if left < right:
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def solution(numbers):
    answer = ''
    merge_sort(numbers, 0, len(numbers)-1)
    numbers = list(map(str, numbers))
    answer = ''.join(numbers)
    return str(int(answer))