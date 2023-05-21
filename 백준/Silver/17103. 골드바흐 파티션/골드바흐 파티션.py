import sys
input=sys.stdin.readline
prime =[True]*1000001
prime[0] = False
prime[1] = False
for i in range(2,1000001):
    if prime[i]:
        for j in range(i*2,1000001,i):
            prime[j]=False
t = int(input())
for i in range(t):
    count=0
    a = int(input())
    for j in range(2,a//2+1):
        if prime[j] and prime[a-j]:
            count+=1
    print(count)
 