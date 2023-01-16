import sys
n = int(sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
B= list(map(int,sys.stdin.readline().rstrip().split()))
A.sort()
def bin_search(num,bound):
    low,high=0,n
    while low<high:
        mid=(low+high)//2
        if bound==0:
            if A[mid]<num:
                low=mid+1
            else:
                high=mid
        else:
            if A[mid]<=num:
                low=mid+1
            else:
                high=mid
    return high
result=[]
for i in B:
    result.append(bin_search(i,1)-bin_search(i,0))
print(*result)
