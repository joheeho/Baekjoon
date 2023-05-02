n = int(input())
min_x,min_y =10000,10000
max_x,max_y =-10000,-10000
for i in range(n):
    a,b = map(int,input().split())
    if a<min_x:
        min_x=a
    if a>max_x:
        max_x=a
    if b<min_y:
        min_y=b
    if b>max_y:
        max_y=b
print((max_x-min_x)*(max_y-min_y))