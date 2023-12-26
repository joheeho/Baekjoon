n = int(input())
data = list(map(int,input().split()))
stack = [ ]
num = 1

for i in range(1,n+1):
    x = data[i-1]
    while  ( stack != [] and stack [-1] == num):
        stack.pop()
        num +=1
    if data[i-1]== num:
        num+=1
    else:
        stack.append(x)

while stack:
    if stack[-1] == num:
        stack.pop()
        num += 1
    else:
        break

if num - 1 == n:
    print("Nice")
else:
    print("Sad")