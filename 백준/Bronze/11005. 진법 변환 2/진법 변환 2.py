number,n =map(int,input().split())
system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
value =''
while number != 0:
    value+=str(system[number%n])
    number//=n 
print(value[::-1])