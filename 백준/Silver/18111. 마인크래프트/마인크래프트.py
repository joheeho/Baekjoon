import sys
n, m, b = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = sys.maxsize
time=0
for now_zone in range(257):
    add,broke=0,0
    for x in range(n):
        for y in range(m):
            if now_zone <= arr[x][y]:    # 배열 값이 현재 층보다 크거나 같을 때
                broke+=(arr[x][y]-now_zone)
            else:    # 배열 값 이 현재층  작을 때
                add+=(now_zone-arr[x][y])
    if b+broke>=add:
        if add + (broke * 2) <= answer:
        	# 0부터 256층까지 비교하므로 업데이트 될수록 고층의 최저시간
            answer = add + (broke * 2) # 최저 시간
            idx = now_zone# 층수
print(answer,idx)
           
