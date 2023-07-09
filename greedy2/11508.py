n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
num = n - n%3
# print(num)
res=0
for i in range(0,num,3):
    min_price = min(arr[i],arr[i+1],arr[i+2])
    # print(min_price)
    res+= arr[i]+ arr[i+1]+arr[i+2]-min_price
    
for i in range(num,n):
    res += arr[i]
print(res)