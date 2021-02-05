# Contest: https://codeforces.com/contest/1481
# Problem: https://codeforces.com/contest/1481/problem/A
# Trials: 3
# Solved: during contest

t = int(input())

for _ in range(t):
  px, py = map(int, input().split())
  str = input()

  u, d, r, l = 0, 0, 0, 0
  if px > 0:
    r = px
  elif px < 0:
    l = -px

  if py > 0:
    u = py
  elif py < 0:
    d = -py

  res = "NO"
  for s in str:
    if s == "R":
      r -= 1
    elif s == "L":
      l -= 1
    elif s == "U":
      u -= 1
    else: # S == "D"
      d -= 1
      
    if r <= 0 and l <= 0 and u <= 0 and d <= 0:
      res = "YES"
      break
      
  print(res)