N,M = map(int,input().split())
j=int(input())
current = 1
ans = 0


for i in range(j):
    apple = int(input())
    if current <= apple <= current+M-1:
        continue
    elif apple<current:
        ans += current - apple
        current -= current -apple
    else:
        ans += apple - (current+M-1)
        current +=apple - (current+M-1)

print(ans)

