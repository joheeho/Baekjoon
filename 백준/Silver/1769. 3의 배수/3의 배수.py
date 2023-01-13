x=input()
def plus_x(x):
    total=0
    for s in x:
        total+=int(s)
    return str(total)
count=0
while len(x)>1:
    count+=1
    x=plus_x(x)
print(count)
if int(x)%3==0:
    print("YES")
else:
    print("NO")
