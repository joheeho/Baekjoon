n,m = map(int,input().split())
coin=[]
index=0
for i in range(n):
    a=int(input())
    if a < m:
        index = i
    else:
        index=i
    coin.append(a)
count=0
while m >0:
    a=m//int(coin[index])
    count+=a
    m-=coin[index]*a
    index-=1;
print(count)
