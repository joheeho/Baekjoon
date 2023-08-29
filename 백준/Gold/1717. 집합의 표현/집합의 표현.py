import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n,m = map(int,input().split())
parent_graph =[ i for i in range(n+1)] 

def find(v): # 부모 구하는 함수 
    if v == parent_graph[v]:
        return v 
    else:
        parent_graph[v] = find(parent_graph[v])
        return  parent_graph[v]
    
for i in range(m):
    a,b,c = map(int,input().split())
    if a == 0:
        parent_graph[ find(b)] = find(c)    
    else:
        if find(b) == find(c):
            print("yes")
        else:
            print("no")
