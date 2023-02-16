import sys
input = sys.stdin.readline
n=int(input())
data=list(map(int,input().split()))  
data1=sorted(list(set(data)))   
score=dict()
for i in range(len(data1)):
    score[data1[i]]=i
for i in data:
    print(score[i],end=' ')
