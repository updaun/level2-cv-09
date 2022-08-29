# source: https://www.acmicpc.net/problem/1003

# N번째 피보나치 수를 구하는 c++ 함수
'''
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
'''

# N이 주어지고 fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하기

'''
입력
첫째 줄: 테스트 케이스 개수 T
각 테스트 케이스 한 줄로 N이 주어진다. (0<= N <= 40)

출력
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력
'''

memo = [[0, 0] for _ in range(41)]

memo[0][0] = 1
memo[1][1] = 1

for i in range(0, 41):

    if i < 40:
        if i != 0: 
            memo[i+1][0] += memo[i][0]
            memo[i+1][1] += memo[i][1]

    if i < 39:
        memo[i+2][0] += memo[i][0]
        memo[i+2][1] += memo[i][1]

t = int(input())

for i in range(t):
    n = int(input())

    print(memo[n][0], memo[n][1])