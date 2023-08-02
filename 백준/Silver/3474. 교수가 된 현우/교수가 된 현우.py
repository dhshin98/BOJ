import sys

n = int(sys.stdin.readline())

def solve(num):
    cnt = 0
    five = 5
    while five <= num: 
        cnt += num //five
        five *= 5
      
    print(cnt)


for i in range(n):
    number =(int(sys.stdin.readline()))
    solve(number)
    