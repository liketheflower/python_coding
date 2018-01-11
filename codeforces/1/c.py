import sys
A = raw_input().split()
B = raw_input().split()
n_type, volume = int(A[0]), int (A[1])
#volume = int(raw_input())
cost = [int(_) for _ in B]
def dp(idx, volume):
    if (idx,volume) not in memo:
        if volume-vol_cost[idx][0] < -2**(n_type-1):
            memo[(idx, volume)] = dp(idx+1,volume)
            return memo[(idx,volume)]
        if sum([vol for vol,_ in vol_cost[idx:]])<volume:
            memo[(idx,volume)] = sys.maxint
            return sys.maxint 
        if len(vol_cost)-idx ==1:
            memo[(idx,volume)] = vol_cost[-1][1]
            return memo[(idx,volume)]
        memo[(idx,volume)] = min(vol_cost[idx][1] + dp(idx+1,volume-vol_cost[idx][0]), dp(idx+1,volume))
    return memo[(idx,volume)]
vol_cost =[]
for i in xrange(len(cost)):
    for j in xrange(1+volume>>i):
       vol_cost.append(((j+1)*1<<i ,cost[i]*(j+1)))
print vol_cost
print len(vol_cost)
vol_cost.sort(reverse=True)

memo = {}
print vol_cost[0][1]
print type(vol_cost[0][1])
print type(dp(1,volume-vol_cost[0][0]))
print vol_cost[0][1] + dp(1,volume-vol_cost[0][0])
if volume-vol_cost[0][0] < -2**(n_type-1):
    min_cost = dp(1,volume)
else:
    min_cost = min(vol_cost[0][1] + dp(1,volume-vol_cost[0][0]), dp(1,volume))
print memo
