import bisect
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
c1, c2 = map(int, input().split())
pset = sorted(list(map(int, input().split())))
qset = sorted(list(map(int, input().split())))

dist = float('inf')
cnt = 0
for p in pset:
    right = bisect.bisect_left(qset, p)
    delta = 1
    if right == m:
        right -= 1
        
    cur_dist = abs(p - qset[right])
    if right:
        left = right - 1
        left_dist = abs(p - qset[left])
        if left_dist < cur_dist:
            cur_dist = left_dist
        elif left_dist == cur_dist:
            delta = 2
    
    if cur_dist < dist:
        dist = cur_dist
        cnt = delta
    elif cur_dist == dist:
        cnt += delta
    
print(dist + abs(c1 - c2), cnt)

