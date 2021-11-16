import sys
input = sys.stdin.readline

N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N+1)]
# row: length of numer
# column: start digit of number

dp[1] = [1 for _ in range(10)]
for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]    
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            
print((sum(dp[N]) - dp[N][0]) % 1000000000)