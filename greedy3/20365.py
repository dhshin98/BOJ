n = int(input())
arr = list(input())

arr.append('0')
cnt_b=1
for i in range(n):
    if arr[i] == 'B':
        continue
    elif arr[i] == 'R':
        cnt_b += 1
        if arr[i+1] == 'R':
            cnt_b -= 1
            continue

cnt_r = 1

for i in range(n):
    if arr[i] == 'R':
        continue
    elif arr[i] == 'B':
        cnt_r += 1
        if arr[i+1] == 'B':
            cnt_r -= 1
            continue

print(min(cnt_b,cnt_r))


