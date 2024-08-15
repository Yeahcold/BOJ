# 계단 오르기
import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())
data = [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(data))
else:
    d = [0] * n
    d[0] = data[0]
    d[1] = max(data[0] + data[1], data[1])
    d[2] = max(data[0] + data[2], data[1] + data[2])

    for i in range(3, n):
        d[i] = max(d[i-2] + data[i], d[i-3] + data[i-1] + data[i])

    print(d[n-1])
