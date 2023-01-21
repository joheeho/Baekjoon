import sys
n,m=map(int,sys.stdin.readline().split())
data={}
for i in range(n):
    email,password= sys.stdin.readline().split()
    data[email]=password
for _ in range(m):
    information=sys.stdin.readline().rstrip()
    print(data[information])
