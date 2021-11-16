import sys
input = sys.stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[0] = wines[0]
    elif i == 1:
        dp[1] = wines[0] + wines[1]
    elif i == 2:
        dp[2] = max(wines[0] + wines[1], wines[1] + wines[2], wines[0] + wines[2])
    else:
        dp[i] = max(dp[i-1], dp[i-2]+wines[i], dp[i-3]+wines[i-1]+wines[i])

print(dp[n-1])