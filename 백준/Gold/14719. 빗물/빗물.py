a,b = map(int,input().split())
data = list(map(int,input().split()))
cnt = 0 
for i in range(1,len(data)-1):
    left_wall = max(data[:i])
    right_wall = max(data[i+1:])
    min_wall = min(left_wall,right_wall)
    if data[i] < min_wall:
        cnt += min_wall-data[i]
print(cnt)
