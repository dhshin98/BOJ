import sys

n = int(sys.stdin.readline())
p1, p2 = map(int, sys.stdin.readline().split())
rel = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]

for i in range(rel):
    n1, n2 = map(int,sys.stdin.readline().split())
    # graph 생성
    graph[n1].append(n2)
    graph[n2].append(n1)

# 가장 인접한 노드끼리 탐색
visited = [False] * (n+1)

def bfs(v, cnt):
    cnt += 1
    visited[v] = True

    if v ==  p2:
        return cnt-1
    for i in graph[v]:
        if not visited[i]:
            result = bfs(i,cnt)
            if result is not None:
                return result

res= bfs(p1,0)
if res is None:
    res = -1

print(res)