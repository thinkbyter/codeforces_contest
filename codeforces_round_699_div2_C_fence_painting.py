# Contest: https://codeforces.com/contest/1481
# Problem: https://codeforces.com/contest/1481/problem/C
# Attempts: 1
# Solved: after contest
# Duration: 02:07:12

from collections import Counter

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  ax = list(map(int, input().split()))
  bs = list(map(int, input().split()))
  cs = list(map(int, input().split()))  
  
  ac = {}
  bc = {}
  dc = {}
  for i, a in enumerate(ax):
    if a in ac:
      ac[a].append(i)
    else:
      ac[a] = [i]
      
    b = bs[i]
    if b in bc:
      bc[b].append(i)
    else:
      bc[b] = [i]
      
    if a != b:
      if b in dc:
        dc[b].append(i)
      else:
        dc[b] = [i]
  
  cc = {}
  for i, c in enumerate(cs):
    if c in cc:
      cc[c].append(i)
    else:
      cc[c] = [i]
  
  msg = "YES"
  if cs[-1] not in bs:
    msg = "NO"
    
  if msg == "YES":
    for k, v in dc.items():
      if k not in cc or len(cc[k]) < len(v):
        msg = "NO"
        break
    
  print(msg)
  if msg == "YES":
    # How to colour the differences.
    res = [-1] * m
    for k, v in dc.items():
      for i, dc_idx in enumerate(v):
        res[cc[k][i]] = dc_idx + 1
    
    # How to colour the remaining.
    if res[-1] == -1:
      res[-1] = bc[cs[-1]][0] + 1
    for i in range(-2, -m - 1, -1):
      if res[i] == -1:
        res[i] = res[i + 1]
    
    print(" ".join(map(str, res)))