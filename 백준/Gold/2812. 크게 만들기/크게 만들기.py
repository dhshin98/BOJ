import sys

n, k = map(int,sys.stdin.readline().split())
num = list(sys.stdin.readline()) 

stack = []

for i in range(n): 
    # 작은 k 개 앞에서부터 삭제하기
    while k>0:
        if stack and stack[-1] < num[i]:
            stack.pop()
            k-=1
        else: 
            break
    stack.append(num[i])

if k > 0:
    print("".join(stack[:-k]))
else:
    print("".join(stack))