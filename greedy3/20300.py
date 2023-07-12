n = int(input())
arr = []
arr = list(map(int,input().split()))

arr.sort()
res = arr[n-1] # 가장 큰 값

if n%2 == 1 :
    for i in range(int(n/2)):
        tmp = arr[i] + arr [n-i-2]
     
        if tmp > res: 
            res = tmp
    print(res)

else: 
    for i in range(int(n/2)):   
        tmp = arr[i] + arr [n-i-1]

        if tmp > res: 
            res = tmp
    print(res)