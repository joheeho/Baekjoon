t=int(input())
zero = [ 0 for i in range(41)]
one =  [ 0 for i in range(41)]
for i in range(t):
    n=int(input())
    zero[0]=1
    one[0]=0
    zero[1]=0
    one[1]=1
    if n==1 or n==0:
        print(zero[n],one[n])
    else:
        for i in range(2,n+1):
            if (i <=n):
                zero[i]=one[i-1]
                one[i]=one[i-1]+one[i-2]
            else:
                break
        print(zero[n],one[n])
