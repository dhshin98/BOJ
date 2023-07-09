n = int(input())
cost=[]
weight=[]
cost = list(map(int,input().split())) # n-1
weight = list(map(int,input().split()))  # n

min_weight = weight[0]
res = cost[0] * weight[0]

#weight로 
for i in range(1,n-1):
    if weight[i]<min_weight:
        min_weight = weight[i]
    res += min_weight * cost[i]

print(res)
