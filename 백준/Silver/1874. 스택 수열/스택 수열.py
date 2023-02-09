n=int(input())
stack=[]
answer=[]
flag=0
count=1
for i in range(1,n+1):
    a=int(input())
    while count <= a:
        stack.append(count)
        answer.append("+")
        count+=1
    if stack[-1] == a:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag=1
        break
if flag !=1:
    for i in answer:
        print(i)

