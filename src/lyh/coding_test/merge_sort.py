def merge(arr, left, mid, right):
    left_pos, right_pos = left, mid + 1
    sorted_list = list()

    while left_pos <= mid and right_pos <= right:
        if arr[left_pos] < arr[right_pos]:
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
        # print("merge b ", arr, left, mid, right)
        merge(arr, left, mid, right)
        # print("merge a ", arr, left, mid, right)

if __name__ == "__main__":
    arr = [21, 10, 12, 20, 1, 25, 13, 15, 22]
    merge_sort(arr, 0, 8)
    print(arr)