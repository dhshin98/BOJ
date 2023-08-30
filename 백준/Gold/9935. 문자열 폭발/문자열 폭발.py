import sys

input = sys.stdin.readline

def solve(s1, check):
    stack = []
    
    for char in s1:
        stack.append(char)
        
        if len(stack) >= len(check) and ''.join(stack[-len(check):]) == check:
            for _ in range(len(check)):
                stack.pop()
    
    return ''.join(stack)


s1 = input().rstrip()
check = input().rstrip()

removed = solve(s1, check)

if removed == "":
    print("FRULA")
else:
    print(removed)
