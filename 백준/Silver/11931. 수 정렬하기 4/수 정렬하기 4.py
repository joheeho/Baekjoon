import sys
a=int(sys.stdin.readline())
data = [int(sys.stdin.readline().strip()) for i in range(a)]
data.sort(reverse=True)
for x in data:
    print(x)
