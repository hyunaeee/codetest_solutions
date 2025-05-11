n = input()
x,y=1,1
direction= input().split()

dx=[0,0,-1,1]
dy=[-1,1,0,0]
movement=['L','R','U','D']

for a in direction:
    for i in range(len(movement)):
        if direction == movement[i]:
            nx = x + dx[i]
            ny = y + dy[i]