import sys

n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
add, sub, mul, div = map(int,sys.stdin.readline().split())

maximum = -1e9 
minimum = 1e9 

def dfs(i,tmp):
    global minimum, maximum, add, sub, mul, div
    if i == n: 
        minimum = min(minimum,tmp)
        maximum = max(maximum, tmp)

    else:
        if add > 0: 
            add -= 1 
            dfs(i + 1, tmp + num[i]) 
            add += 1 
        if sub > 0:
            sub -=1 
            dfs(i+1,tmp - num[i])
            sub += 1
        if mul > 0:
            mul -=1 
            dfs(i+1,tmp * num[i])
            mul += 1
        if div > 0:
            div -=1 
            dfs(i+1,int(tmp / num[i]))
            div += 1

        
dfs(1, num[0])
print(int(maximum))
print(int(minimum))