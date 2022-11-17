a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
g=int(input())
fuc=[a,b,c,d,e,f,g]
odd=[]
for i in range(len(fuc)):
    if fuc[i]%2 !=0:
        odd.append(fuc[i])
odd.sort()
if odd ==[]:
    print("-1")
else:
    print(sum(odd))
    print(odd[0])

        
    
        