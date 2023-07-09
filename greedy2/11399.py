N = int(input())
arr = []

arr = list(map(int,input().split()))

arr.sort(reverse = False) 


res = 0
for i in range(N):
    res+= arr[i] * (N -i)

print(res)
