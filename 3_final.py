def moocount(N, F, sss):
    result = set()
    ptp = {}
    
    for i in range(N - 2):
        if sss[i+1] == sss[i+2] and sss[i] != sss[i+1]:
            pt = sss[i:i+3]
            if pt not in ptp:
                ptp[pt] = []
            ptp[pt].append(i)
    
    for pt, p in ptp.items():
        if len(p) >= F:
            result.add(pt)
    
    for i in range(N):
        o = sss[i]
        affected_range = range(max(0, i-2), min(N-2, i+1))
        
        affected_pt = set()
        for j in affected_range:
            if j+2 < N and sss[j+1] == sss[j+2] and sss[j] != sss[j+1]:
                affected_pt.add(sss[j:j+3])
        
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c == o:
                continue
            
            ptc = {}
            
            for pt, p in ptp.items():
                ptc[pt] = len(p)
            
            for j in affected_range:
                if j+2 < N and sss[j:j+3] in affected_pt:
                    ptc[sss[j:j+3]] -= 1

                ns = sss[j:i] + c + sss[i+1:j+3] if i in range(j, j+3) else sss[j:j+3]
                if len(ns) == 3 and ns[1] == ns[2] and ns[0] != ns[1]:
                    ptc[ns] = ptc.get(ns, 0) + 1
            
            for pt, count in ptc.items():
                if count >= F:
                    result.add(pt)
    
    return sorted(list(result))

N, F = map(int, input().split())
sss = input().strip()

result = moocount(N, F, sss)
print(len(result))
for moo in result:
    print(moo)
