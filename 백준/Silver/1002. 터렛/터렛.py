import math
t = int(input())
for i in range(t):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    distance = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
    if x1 == x2 and y1 == y2:   # 조규현과 백승환의 좌표가 같을때
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:  #다를떄
        if r1+r2 < distance:
            print(0)
        else:
            if max(r1,r2)-min(r1,r2) > distance:
                print(0)
            else:
                if r1+r2 == distance:
                    print(1)
                elif max(r1,r2)-min(r1,r2) ==distance:
                    print(1)
                else:
                    print(2)
        
