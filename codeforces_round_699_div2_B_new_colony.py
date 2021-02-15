# Contest: https://codeforces.com/contest/1481
# Problem: https://codeforces.com/contest/1481/problem/B
# Attempts: 4
# Solved: during contest

t = int(input())

for _ in range(t):
  n, k = map(int, input().split())
  hs = list(map(int, input().split()))
  stops = [i < n - 1 and h < hs[i + 1] for i, h in enumerate(hs)]
  
  p = -1
  for i, stop in enumerate(stops):
    if stop:
      p = i
      break

  if p != -1:
    while k > 0 and p != -1:
      h = hs[p]
      
      next_h = hs[p + 1]
      next_diff = next_h - h
      
      prev_h = None if p == 0 else hs[p - 1]
      prev_diff = None if prev_h is None else prev_h - h
      
      if prev_diff is None or prev_diff >= next_diff:
        subtract = next_diff
        prev_stop = False
      else:
        subtract = prev_diff + 1
        prev_stop = True
     
      k -= subtract
      
      if k > 0:
        hs[p] += subtract
        stops[p] = hs[p] < hs[p + 1]
        
        prev_p = p
        if prev_stop:
          stops[p - 1] = True
          p -= 1
        else:
          for i, stop in enumerate(stops[p + 1:]):
            if stop:
              p += i + 1
              break
          
          if prev_p == p:
            p = -1
        
  p += 0 if p == -1 else 1
  print(p)