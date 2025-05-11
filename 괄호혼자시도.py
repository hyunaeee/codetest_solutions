while True:
    td=input()
    if td=='.':
        break
    stack=[]
    check = True

    for char in td:
        if '('==char:
            stack.append(char)
        elif '['==char:
            stack.append(char)
        elif ')'==char:
            if len(stack)>0 and stack[-1]=='(':
                stack.pop()
            else:
                check = False
                break

        elif ']'==char:
            if len(stack)>0 and stack[-1]=='[':
                stack.pop()
            else:
                check = False
                break

    if len(stack)==0 and check==True:
        print('yes')
    else:
        print('no')

        