import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))

data.sort()

cnt = 0
# tmp = 0
# end = 0
start = 0
end = n-1

while start < end:
    if data[start] + data[end] == m:
        cnt += 1
        start += 1
        end -= 1
    elif  data[start] + data[end] < m:
        start +=1
    else: 
        end -=1

# for start in range(n):
#     while tmp<m and end<n:
#         tmp += data[end]
#         end += 1
#     if tmp == m:
#         cnt += 1
#     tmp -= data[start]

print(cnt)