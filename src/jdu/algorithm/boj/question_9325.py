import sys
t = int(sys.stdin.readline())
for i in range(t):
    car_price = int(sys.stdin.readline())
    opt = int(sys.stdin.readline())
    for j in range(opt):
        n, opt_price = list(map(int, sys.stdin.readline().split()))
        car_price += n*opt_price
    print(car_price)
    