import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

def getTree(h):
    ret = 0
    for t in trees:
        if t > h:
            ret += t - h
            
    return ret

lh, rh = (0, 1000000000)
answer = 0
while lh <= rh:
    mid = (lh + rh) // 2
    if getTree(mid) >= M:
        answer = mid
        lh = mid + 1
    else:
        rh = mid - 1

print(answer)