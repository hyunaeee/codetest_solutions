import sys
input = sys.stdin.readline

def cube():
  N, Q = map(int, input().split())
  grp = {}
  count = 0
  for _ in range(Q):
    x, y, z = map(int, input().split())
    ks = [f"x{x}y{y}", f"y{y}z{z}", f"x{x}z{z}"]
    for k in ks:
      if k in grp:
        grp[k] += 1
        if grp[k] == N:
          grp.pop(k)
          count+=1
      else:
        grp[k] = 1
    print(count)

cube()

