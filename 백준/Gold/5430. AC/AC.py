import sys
from collections import deque

t=int(sys.stdin.readline())
for i in range(t):
    error=0
    reverse_count=0
    command= sys.stdin.readline().rstrip()
    n=int(sys.stdin.readline().rstrip())
    string=deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    if n==0:                   # 빈 값인 경우 
        string=[]
    for x in command:
        if x=='R':
            reverse_count+=1
        else:
            if len(string)==0:
                print("error")
                error=1
                break
            else:
                if reverse_count%2==0:
                    string.popleft()
                else:
                    string.pop()
    else:
        if reverse_count%2==0:
            print("["+",".join(string)+"]")   
        else:
            string.reverse()
            print("["+",".join(string)+"]")   