n,m=map(int,input().split())

result=0

for i in range(n):#줄마다
    data = list(map(int,input().split()))#입력받아서
    minv = min(data)#가장작은거찾고
    result=max(result, minv)#그중에 가장 큰거

print(result)


#다른 답안
for i in range(n):
    data=list(map(int,input().split()))
    minv=10001 #최대10000이라서
    for a in data: #한줄중에
        minv=min(minv,a) #가장 작은거 찾아서
    result=max(result,minv) #가장 큰 지

print(result)
