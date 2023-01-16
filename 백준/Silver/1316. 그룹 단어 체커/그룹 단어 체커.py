n=int(input())
group_word=0
for i in range(n):
    data=input() 
    if len(data)<=2:
        group_word+=1
    else:
        error=0
        for j in range(len(data)-1):
            if data[j] == data[j+1]:
                continue
            elif data[j] in data[j+1:]:
                error=1
                break
        if error ==0:
            group_word+=1

print(group_word)

            

            