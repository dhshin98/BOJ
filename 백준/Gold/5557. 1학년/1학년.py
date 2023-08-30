import sys
input=sys.stdin.readline

n=int(input())
dp=[[0 for _ in range(n)] for _ in range(21)]  # 0-20 row, n col
arr=list(map(int, input().split()))

dp[arr[0]][0]=1

for i in range(1, n-1):
    for j in range(21):

        if 0 <= j + arr[i] <= 20:
            dp[j+arr[i]][i] += dp[j][i-1]
        if 0 <= j - arr[i] <= 20:
            dp[j-arr[i]][i] += dp[j][i-1]


print(dp[arr[n-1]][n-2]) # arr[n-1]행  n-2 열
