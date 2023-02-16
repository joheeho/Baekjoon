import sys
n=int(sys.stdin.readline().rstrip())
list_1=[]
for i in range(n):
    list_1.append(sys.stdin.readline().rstrip())
list_1=list(set(list_1))
list_1.sort()
list_1.sort(key=len)
for i in list_1:
    print(i)
