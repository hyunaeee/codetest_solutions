#내 풀이
n,k=map(int,input().split())
count=0

while n!=1:
    count+=1
    if n%k==0:
        n=n//k
    else:
        n-=1

print(count)


#다른 답안 (숫자가 더 클떄는 배수로 만들어서)
result=0
while True:
    target=(n//k)*k
    result+=(n-target)
    n=target

    if n<k:
        break
    result +=1
    n//=k

    result += (n-1)
    print(result)

