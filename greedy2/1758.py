n = int(input())
arr = []
for i in range(n):
    arr.append( int(input()))

arr.sort(reverse=True)
res = 0
for i in range(n):
    tmp = arr[i] - i
    if(tmp<0):
        tmp = 0
    res += tmp

print(res)