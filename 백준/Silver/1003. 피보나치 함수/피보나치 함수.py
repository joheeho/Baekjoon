t=int(input())
zero = [ 0 for i in range(41)]
one =  [ 0 for i in range(41)]
for i in range(t):
    n=int(input())
    for i in range(0,n+1):
        zero[0]=1
        one[0]=0
        zero[1]=0
        one[1]=1
        if n>=2:
            zero[i]=one[i-1]
            one[i]=one[i-1]+one[i-2]
    print(zero[n],one[n])
