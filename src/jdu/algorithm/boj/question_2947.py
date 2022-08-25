n_list = list(map(int, input().split()))
while n_list != [1, 2, 3, 4, 5]:
    for i in range(4):
        if n_list[i] > n_list[i+1]:
            temp = n_list.pop(i)
            n_list.insert(i+1, temp)
            print(" ".join(map(str, n_list)))