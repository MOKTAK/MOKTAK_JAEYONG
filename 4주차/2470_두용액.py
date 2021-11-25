import sys
input = sys.stdin.readline

N = int(input())
liq = list(map(int, input().split()))
liq.sort()


li, ri = (0, N-1)
lastv = liq[ri] + liq[li]
la, ra = (li, ri)

while li < ri:
    cursum = liq[li] + liq[ri]
    if abs(lastv) > abs(cursum):
        la, ra = li, ri
        lastv = cursum
        if lastv == 0: break
    
    if cursum > 0:
        ri -= 1
    else:
        li += 1
    

print(liq[la], liq[ra])