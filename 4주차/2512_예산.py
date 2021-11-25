import bisect
import sys
input = sys.stdin.readline

N = int(input())
local = sorted(list(map(int, input().split())))
maximum = int(input())

l, r = (0, local[N-1])
answer =  0
while l <= r:
    m = (l + r) // 2
    lower = bisect.bisect_right(local, m)
    
    total = sum(local[:lower]) + (N - lower) * m
    if lower == N or total == maximum:
        answer = m
        break
    
    if total > maximum:
        r = m - 1
    else:
        answer = m
        l = m + 1
    
print(answer)
