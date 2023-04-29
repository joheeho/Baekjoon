n=int(input())
for i in range(n):
    a = int(input())
    print(a//25, (a%25) //10 , ((a%25)%10) //5, (((a%25)%10)%5))
