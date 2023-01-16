import sys
n = int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
target_data = list(map(int,sys.stdin.readline().rstrip().split()))
score=[]
data.sort()
def bin_search(data,x):
    count=0
    low=0
    high=len(data)-1
    while low<=high:
        mid=(low+high)//2
        if x==data[mid]:
            count+=1
            return count
        elif x>data[mid]:
            low=mid+1
        else:
            high=mid-1
    return 0
for i in range(len(target_data)):
    print(bin_search(data,target_data[i]),end=' ')