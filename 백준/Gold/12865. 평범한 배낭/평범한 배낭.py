import sys
# sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
# p[n] = max ( p[n-1, w], p[n-1,w-w_i] + p_i)
# c가 최소 profit이라고 생각하면 됨.
cost = []
profit = []
res = [[0] * (k+1) for _ in range(n+1)]
for i in range(n):
    cost_n, profit_n = map(int, input().split())
    cost.append(cost_n)
    profit.append(profit_n)
#여기까지가 초기 구성.
for i in range(1, n+1):
    for j in range(k+1):
        if j < cost[i-1]:
            res[i][j] = res[i-1][j]
        else:
            res[i][j] = max(res[i-1][j], res[i-1][j-cost[i-1]] + profit[i-1])
print(res[n][k])



