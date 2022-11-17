x,y,w,h=map(int,input().split())
right=w-x #현재 위치에서 직사각형의 경계선까지 오른쪽 길이  
left=x    #현재 위치에서 직사각형의 경계선까지 왼쪽 길이
up=h-y    #현재 위치에서 직사각형의 경계선까지 위쪽 길이
down=y    #현재 위치에서 직사각형의 경계선까지 아래쪽 길이
print(min(right,left,up,down))