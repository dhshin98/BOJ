import sys
import math
input = sys.stdin.readline

n, bridge = map(int, input().split())

water = []

for i in range(n):
   water.append(list(map(int, input().split())))

water.sort()

count = 0
index = 0 

for start,end in water:
    if start <= index:
        start = index + 1

    tempcnt = math.ceil((end-start) / bridge)
    count += tempcnt
    index = max (index, start + tempcnt * bridge-1)
    

print(count)