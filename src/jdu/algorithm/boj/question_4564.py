while True:
    num = str(input())
    num_list = [num]
    if num == "0":
        break
    while len(num) != 1:
        temp = 1
        for i in range(len(num)):
            temp *= int(num[i])
        num_list.append(temp)
        num = str(temp)
    print(" ".join(map(str, num_list)))