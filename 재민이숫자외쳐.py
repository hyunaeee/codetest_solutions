K=int(input())
st =[]

for _ in range(K):
    num = int(input())
    if num != 0:
        st.append(num)
    elif num == 0:
        st.pop()

print(sum(st))