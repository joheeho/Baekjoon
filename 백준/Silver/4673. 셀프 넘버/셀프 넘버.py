lst = [ ] 
def selfnum(n):
    num = int(n)
    for i in range(len(n)):
        num +=int(n[i])
    lst.append(num)
    return lst

for i in range(1,10000):
    selfnum(str(i))


for i in range(1,10001):
    if i not in lst:
        print(i)


