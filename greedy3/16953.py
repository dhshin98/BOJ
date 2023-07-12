a,b = map(int,input().split())

res =0

while True:
    res+=1
    tmp = b
    if(b%10 == 1):
        b= int(b/10)
    elif b%2 == 0:
        b = int(b/2)

    if b==a: 
        res+=1
        print(res)
        break

    if b==0 or tmp ==b:
        print(-1)
        break
  
