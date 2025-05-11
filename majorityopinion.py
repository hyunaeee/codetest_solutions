# from collections import Counter
# T= int(input())

# def solve():
#     if 

# for _ in range(T):
#     N= int(input())
#     testcase= list(map(int, input().split())) #혹은 =[int(x) for x in input().split()]


for i in range(int(input())):
    N = int(input())
    seq = list(map(int, input().split()))
    doable = []

    if N < 3:
        print(-1)
        continue
    for i in range(N-1):
        if seq[i+2] == seq[i+1]:
            if not(seq[i+2] in doable):
                doable.append(seq[i+2])
        elif seq[i+2] == seq[i]:
            if not(seq[i+2] in doable):
                doable.append(seq[i+2])
        elif seq[i] == seq[i+1]:
            if not(seq[i] in doable):
                doable.append(seq[i])

    
    if len(doable) == 0:
        print(-1)
        continue

    for i in range(len(doable)):
        print(doable[i], end=" ")
    print()