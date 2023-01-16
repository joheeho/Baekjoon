import sys
n = int(sys.stdin.readline().rstrip())
data = set(map(int,sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
target_data = list(map(int,sys.stdin.readline().rstrip().split()))
answer=[]
for i in range(m):
    if target_data[i] in data:
        answer.append('1')
    else:
        answer.append('0')
answer=' '.join(answer)
print(answer)