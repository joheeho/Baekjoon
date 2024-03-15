data = list(map(int,input().split()))
while data[0] != 0:
    leaf = 1 
    for i in range(1,len(data)):
        if i % 2 != 0: 
            leaf *=data[i]
        else:
            leaf-=data[i]
    print(leaf)
        
    data = list(map(int,input().split()))

