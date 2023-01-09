import math
m=int(input())
n=int(input())
data=[]
def countdivisor(n):
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return 0
for i in range(m,n+1):
    if countdivisor(i)!=0:
        data.append(i)
if len(data)!=0:
    print(sum(data))
    print(data[0])
else:
    print(-1)
