from sys import stdin
input = stdin.readline
n,m=map(int,input().split())
data=list(map(int,input().split()))
cumulative_sum=[0]
total=0
for i in range(n):
    total+=data[i]
    cumulative_sum.append(total)
for j in range(1,m+1):
    a,b=map(int,input().split())
    print(cumulative_sum[b]-cumulative_sum[a-1])



  

