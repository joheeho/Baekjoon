import sys
n,m = map(int,input().split())
pokemon=dict()
pokemon1=dict()
for i in range(1,n+1):
    a = str(sys.stdin.readline().rstrip())
    pokemon[a]=i
    pokemon1[i]=a
for i in range(m):
    a = str(sys.stdin.readline().rstrip())
    if 65<=ord(a[0])<=90:
        print(pokemon.get(a))
    else:
        print(pokemon1.get(int(a)))
