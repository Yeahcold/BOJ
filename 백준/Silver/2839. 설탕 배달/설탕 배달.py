# 설탕 배달
import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())

d = [9999] * 5001

d[0] = 0

for i in range(1, n+1):
    d[i] = min(d[i-3] + 1, d[i-5] + 1, d[i])

if d[n] == 9999:
    print("-1")
else:
    print(d[n])