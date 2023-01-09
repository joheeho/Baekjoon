from collections import deque
n,k=map(int,input().split())
que1=[]
q=deque([i for i in range(1,n+1)])
while q:
    q.rotate(-(k-1))
    que1.append(q.popleft())
print(f'<{str(que1)[1:-1]}>')


