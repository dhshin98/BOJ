import sys

n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))

res = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == data[i] and res[j]==0:
            res[j] = i+1
            break
        elif res[j] == 0:
            cnt +=1

print(*res)
