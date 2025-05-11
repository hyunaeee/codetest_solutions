from collections import deque

N=int(input())
q=deque()

for _ in range(N):
    command=input()  
    if "push" in command:
        order,num=command.split()
        num=int(num)
        q.append(num)
    elif command=="pop":
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())
    elif command=="size":
        print(len(q))
    elif command=="empty":
        print(int(len(q)==0))
    elif command=="front":
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif command=="back":
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])


