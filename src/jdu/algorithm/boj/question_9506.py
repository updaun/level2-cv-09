import sys
while True:
    number = int(sys.stdin.readline())
    div_list = [1]
    div = 2
    if number == -1:
        break
    while div < number/2:
        if number % div == 0:
            div_list.append(div)
            div_list.append(number//div)
        div += 1
    target = sorted(list(set(div_list)))
    if number == sum(target):
        print(f"{number} = "+" + ".join(map(str, target)))
    else:
        print(f"{number} is NOT perfect.")

# 처음 풀이 : list(set(sorted(div_list)))
# 개선된 풀이 : sorted(list(set(div_list)))
# set을 취한 뒤에 list를 하면 순서가 섞여 버리는 문제 발생