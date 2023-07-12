N = int(input())
arr = []
arr = list(map(int,input().split()))
arr.sort()

res = 0
for i in range(N-1):
    res += arr[i]/2

res +=arr[N-1]
print(res)