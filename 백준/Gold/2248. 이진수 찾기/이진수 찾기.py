# 참고한 사이트
# https://velog.io/@cchloe2311/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-2248.-%EC%9D%B4%EC%A7%84%EC%88%98-%EC%B0%BE%EA%B8%B0

import sys

N,bit,find = map(int, sys.stdin.readline().split())

dp = [[0] * 32 for _ in range(32)]

for i in range(31):
    dp[0][i] = 1
for i in range(1,32):
    dp[i][0] = dp[i-1][0]
    for j in range(1,32):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

result = []
for pos in range(N, 0, -1):
    if find <= dp[pos-1][bit]: 
        digit = 0
    else: 
        digit = 1
        find -= dp[pos-1][bit]
        bit -= 1
    
    result.append(digit)
    

print(*result,sep='')