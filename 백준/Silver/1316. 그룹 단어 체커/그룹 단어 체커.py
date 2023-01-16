n=int(input())
group_word=0
for i in range(n):
    data=input() 
    if len(data)<=2:
        group_word+=1
    else:                              
        succession_word=1
        for j in range(len(data)-1):
            error=0
            if data[j] == data[j+1]:
                succession_word+=1
            else:
                if data.count(data[j])==succession_word:
                    succession_word=1
                else:
                    error=1
                    break
        if error ==0:
            group_word+=1

print(group_word)

            