import sys

sys.setrecursionlimit(3000)

N, M, K = map(int, input().split())
wanted = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a]+=[b]
    graph[b]+=[a]

visited = [0] * (N + 1)
friends = [] 



def dfs(v, arr):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = 1
            arr.append(i)
            dfs(i, arr)

for i in range(1, N + 1):
    if not visited[i]:
        arr = [i]
        visited[i] = 1
        dfs(i, arr)
        friends.append(arr)

result = 0
for friend in friends:
    cost = 1 << 60
    for j in friend:
        if cost > wanted[j]:
            cost = wanted[j]
    result += cost


if result <= K:
    print(result)
else:
    print("Oh no")
