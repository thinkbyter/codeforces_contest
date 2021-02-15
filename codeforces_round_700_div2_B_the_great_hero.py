# Contest: https://codeforces.com/contest/1480
# Problem: https://codeforces.com/contest/1480/problem/B
# Attempts: 14
# Solved: after contest
# Duration: 01:36:13

ts = int(input())

for t in range(ts):
  A, B, n = map(int, input().split())
  ax = list(map(int, input().split()))
  bs = list(map(int, input().split()))
  
  msg = 'NO'
  for a, b in zip(ax, bs):
    km = b // A
    if b % A != 0:
      km += 1
    # IDEA: make the above more concise.
      
    B -= km * a
    
  if B >= 0:
    msg = 'YES'
  else:
    for a in ax:
      if B + a > 0:
        msg = 'YES'
        break
      
  print(msg)