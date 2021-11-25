import sys
import bisect
input = sys.stdin.readline

N, C = map(int, input().split())
routers = sorted([int(input()) for _ in range(N)])

l, r = (1, routers[-1] - routers[0])
answer = 0
while l <= r:
    m = (l + r) // 2
    cur = routers[0]
    cnt = 1
    for r in routers:
        if r - cur >= m:
            cur = r
            cnt += 1

    if cnt < C:
        r = m - 1
    else:
        answer = m
        l = m + 1

print(answer)
