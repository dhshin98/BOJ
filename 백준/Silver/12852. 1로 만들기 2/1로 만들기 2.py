import sys

n = int(sys.stdin.readline())
cnt = 0
res = []
calc = ["-1"] *(n+1)
dp = [0] *(n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
        if dp[i] == dp[i//2]+1:
            calc[i] = "2"
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
        if dp[i] == dp[i//3]+1:
            calc[i] ="3"


print(dp[n])

while n != 1:
    print(n, end=" ")
    if calc[n] == "-1":
        n -= 1
    elif calc[n] == "2":
        n = n // 2
    else:
        n = n // 3
print(1)