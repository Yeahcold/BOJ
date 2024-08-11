# 2343
import sys
# sys.stdin = open("input.txt", "rt")

def check(capacity, times):
    cnt = 1
    total = 0
    for t in times:
        if total + t > capacity:
            cnt += 1
            total = t
        else:
            total += t
    return cnt

def solution(m, times):
    left = max(times)
    right = sum(times)
    
    while left < right:
        mid = (left+right)//2
        if check(mid, times) <= m:
            right = mid
        else:
            left = mid + 1
    return left
        

n, m = map(int, input().split())
times = list(map(int, input().split()))
print(solution(m, times))