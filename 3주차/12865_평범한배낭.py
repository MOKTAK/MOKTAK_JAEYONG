import sys
input = sys.stdin.readline

N, K = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(K+1)]for _ in range(N)]

for i in range(N):
    w, v = things[i]
    for j in range(K+1):
        if not i: 
            dp[i][j] = v if w <= j else 0
        elif w <= j:
            dp[i][j] = max(dp[i-1][j - w] + v, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[N-1][K])