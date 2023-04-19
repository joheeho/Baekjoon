n,m=map(int,input().split())
lst=[i for i in range(0,n+1)]
for i in range(m):
    a,b,c=map(int,input().split ())
    part_1=lst[a:c]
    part_2=lst[c:b+1]
    lst[a:b+1]=part_2+part_1
lst.remove(lst[0])
print(*lst)
