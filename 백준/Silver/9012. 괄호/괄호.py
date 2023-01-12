n=int(input())
for i in range(n):
    s = 0
    stack=[]
    data=list(input())
    for i in range(len(data)):
        if data[i]=="(":
            stack.append(data[i])
        else:
            if "(" in stack:
                stack.append(data[i])
                stack.pop()
                stack.pop()
            else:
                s =1
    if s !=1:
        if len(stack)==0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
