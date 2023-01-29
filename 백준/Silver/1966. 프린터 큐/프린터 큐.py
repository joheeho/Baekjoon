from collections import deque
t=int(input())
for i in range(t):
    out_count=0
    deque1=deque()
    count,locate=map(int,input().split())
    importance=list(map(int,input().split()))
    importance1=importance[:]
    if len(importance)==len(set(importance)): # 놓인 순서도의 중복이 없을 경우
        target=importance[locate]      # 구하려는 값의 중요도 
        importance.sort(reverse=True)  # 내림차순 정렬
        print(importance.index(target)+1)
    else:    # 순서 중복 존재하는 경우
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
        

