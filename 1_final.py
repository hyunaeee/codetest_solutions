import sys

def round():
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        if len(str(n)) == 1:
            print(0)
            continue
        
        vnum = 0
        for dgtlen in range(2, len(str(n))+1):
            minv = int('4' * (dgtlen-1) + '5')
            maxv = int('4' + '9' * (dgtlen-1))
            if minv <= n:
                if maxv <= n:
                    vnum += maxv - minv + 1
                else:
                    vnum += n - minv + 1
        print(vnum)

round()