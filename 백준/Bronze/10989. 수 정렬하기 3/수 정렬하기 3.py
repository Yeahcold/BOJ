import sys
#sys.stdin = open("input.txt", "rt", encoding="utf-8")

n = int(input())

count = [0] * 10001

for i in range(n):
    num = int(input())
    count[num] += 1
    
for i in range(10001):
    for j in range(count[i]):
        print(i, end = " ")