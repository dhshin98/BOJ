N, K = map(int,input().split())

arr = []

for i in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)
# print(arr)
res = 0
for i in range(N):
    tmp = int(K / arr[i])
    # print("tmp:",tmp)
    res += tmp
    K = K -tmp * arr[i]
    if K ==0:
        break
print(res)