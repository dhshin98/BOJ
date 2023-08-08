import sys

n = int(sys.stdin.readline())
data = []
graph = [[] for i in range(n) ]

for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            graph[i].append(j)

def bfs(v):
    for i in graph[v]:
        if not visited[i] and data[v][i]==1:
            visited[i] =True
            bfs(i)

for i in range(n):
    visited = [False] * n
    bfs(i)
    for j in range(n):
        if visited[j] == True:
            print(1, end = " ")
        else:
            print(0, end = " ")
    print()
    visited = [False] * n