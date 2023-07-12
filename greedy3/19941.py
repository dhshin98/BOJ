n, k = map(int,input().split())
arr = list(input())
# k 까지 reach 가능함
res = 0

for i in range(n):
    if arr[i] == 'P':
        for j in range(max(0,i-k),min(n,i+k+1)):
            if arr[j] == 'H':
                arr[j] = 'D'
                res +=1
                break
print(res)
