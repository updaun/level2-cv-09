# python sort는 어떤 알고리즘을 쓸까?
# https://velog.io/@toezilla/1D1Q-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%98-sort-%EB%82%B4%EC%9E%A5%ED%95%A8%EC%88%98%EB%8A%94-%EC%96%B4%EB%96%A4-%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%A0%EA%B9%8C
# https://d2.naver.com/helloworld/0315536
# timsort = Insert sort + Merge sort
import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    print(sorted(list(map(int, input().split())))[-3])
