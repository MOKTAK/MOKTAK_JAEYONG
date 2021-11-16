import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(3)] for _ in range(N+1)]
dp[1] = cost[0]

for i in range(2, N+1):
    for j in range(3):
        dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + cost[i-1][j]
        
print(min(dp[N]))
# print(dp)