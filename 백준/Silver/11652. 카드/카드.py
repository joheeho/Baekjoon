import sys
input = sys.stdin.readline
n = int(input())
num ={}
for i in range(n):
    a = int(input())
    if a in num:
        num[a]+=1
    else:
        num[a]=1
d1 = dict(sorted(num.items()))
d2 = sorted(d1.items(), key=lambda x: x[1], reverse=True)
print(d2[0][0])
