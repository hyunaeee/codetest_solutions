
# testdata = [input() for _ in range(n)]

n=int(input())

for _ in range(n):
    testdata=input()
    stack=[]
    check = True

    for char in testdata:
        if '('==char:
            stack.append(char)
        elif ')'==char:
            if len(stack)!=0:
                stack.pop()
            else:
                check = False
                break
    if len(stack)==0 and check==True :
        print("YES")
    else:
        print("NO")
