import sys

n = int(sys.stdin.readline())
arr = list( map(int,sys.stdin.readline().split()))
arr.sort()

ans = 0
for i in range(n):
    goal = arr[i]
    start = 0
    end = n-1

    while start< end:
        tempsum = arr[start] + arr[end]
        if tempsum < goal:
            start +=1
        elif tempsum > goal:
            end -=1
        else:
            # 수의 위치가 다르면 값이 같아도 다른 수라는 조건
            # 투 포인터로 검사할 때 현재 검사하고자 하는 숫자는 제외
            if start != i and end != i:
                ans +=1
                break
            if start == i:
                start += 1
            elif end == i:
                end-= 1

print(ans)