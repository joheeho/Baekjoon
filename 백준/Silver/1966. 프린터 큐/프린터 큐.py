from collections import deque
t=int(input())
for i in range(t):
    out_count=0
    count,locate=map(int,input().split())
    importance=list(map(int,input().split()))
    importance1=importance[:]
    deque1=deque()
    for j in range(count):
        deque1.append(j)
    target=deque1[locate]
    while target in deque1:
        first=deque1[0]  # deque 나가려는 처음 값 
        if importance[first]>=max(importance1): # deque의 처음값이 가장 큰 순서인 경우 
                deque1.popleft()
                importance1.remove(importance[first])
                out_count+=1
        else:           # deque 뒤에 더 큰 순서도가 존재하는 경우
                deque1.rotate(-1)
                first=deque1[0]
    print(out_count)
