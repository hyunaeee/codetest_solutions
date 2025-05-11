n,m,k=map(int,input().split()) # n개의 수를 입력 받을 것임, 가장 큰 수 만들게 m개 더할 건데, 연속은 k번 반복 가능
data=list(map(int,input().split())) # n개 입력 받기

data.sort()
first=data[n-1] #biggest num
second=data[n-2] #한번만 끊어가면 되니까 두번째까지만 필요함

result = 0

while True:
    for i in range(k): #가장 큰 수 k번 반복가능하니까
        if m == 0: 
            break #혹시 m개 더하는게 0개면 끝내기
        result += first 
        m-= 1 #카운트용으로 m이 0되면 끝내게 하려고
    if m ==0: break
    result += second #두번째 큰수로 한번 끊어가고 
    m-=1 #카운트 줄이고
    #다시 while로 반복 break걸릴때까지

print(result)


#다른 방법
count = int(m/(k+1))*k #m/(k+1)끊어가는 덩어리 수, 덩어리수에 반복가능 k수 곱하면 =큰수등장 횟수
count += m%(k+1) #안 나누어 떨어지면 나머지 횟수만큼 큰 수 더해져야함

result+= count *first
result+= (m-count)*second