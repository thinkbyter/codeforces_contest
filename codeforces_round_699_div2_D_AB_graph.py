# Contest: https://codeforces.com/contest/1481
# Problem: https://codeforces.com/contest/1481/problem/D
# Attempts: 14
# Solved: after contest
# Duration: 05:07:41

from collections import Counter
import itertools

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  g = []
  acs = []
  bcs = []
  res = []
  if m == 1:
    res = [1, 2]
  for i in range(n):
    if res:
      _ = input()
    else:
      r = input().replace(" ", "")
      
      if i > 0:
        for j in range(i):
          if r[j] == g[j][i]:
            if m % 2 == 0:
              res = [i + 1, j + 1] * (m // 2)
              res.append(i + 1)
            else:
              res = [i + 1, j + 1] * ((m + 1) // 2)
            break
      
      if not res:
        ac = r.count("a")
        acs.append(ac)
        bcs.append(n - 1 - ac)
        g.append(r)
  
  if not res:
    # I know that if ij is a then ji is b and vica versa.
    # 50% a's and 50% b's
    if m % 2 == 1:
      if m % 2 == 0:
        res = [1, 2] * (m // 2)
        res.append(1)
      else: 
        res = [1, 2] * ((m + 1) // 2)
    elif m == 2:
      for i in range(n):
        for j in range(n):
          if i != j:
            c = g[i][j]
            k = g[j].find(c)
            if k != -1:
              res = [i + 1, j + 1, k + 1]
              break

        if res:
          break
    else:
      # If there is no identical letters in loop of size 3, 
      # there is no identical letters in loop of higher size.
      for rs in itertools.permutations(range(n), 3):
        c0 = g[rs[0]][rs[1]]
        c1 = g[rs[1]][rs[2]]
        if c0 == c1:
          c2 = g[rs[2]][rs[0]]
          if c1 == c2:
            l = [rs[0] + 1, rs[1] + 1, rs[2] + 1]
            res = l * ((m + 1) // 3)
            res.extend(l[:(m + 1) % 3])
            break
      
      # The solution is a m+1 length list of numbers from 1 to n+1 (0 to n)
      # where no consecutive numbers can be the same.
      # This is the full solution space.
      # Let's start with the middle.
      for x, y, z in itertools.permutations(range(n), 3):
        # Can it be declared outside of the loop?
        fs = [] # first half
        ss = [] # second half
        f = g[x][y]
        s = g[y][z]
        
        if f == s:
          fs.append(x)
          ss.append(z)
          
          find = False
          l = 2
          r = 0
          c = 0
          while l < m and l >= 2:
            if r == x:
              r += 1
            elif c == z:
              c += 1
            elif r >= n:
              r = 0
              c += 1
            elif c >= n:
              x = fs.pop() + 1
              z = ss.pop()
              r = 0
              c = 0
              l -= 2
            elif x >= n:
              x = 0
              z += 1
              r = 0
              c = 0
            elif z >= n:
              x = fs.pop() + 1
              z = ss.pop()
              r = 0
              c = 0
              l -= 2
            else:
              f = g[r][x]
              s = g[z][c]
              if f == s:
                fs.append(r)
                ss.append(c)
                x = r
                z = c
                r = 0
                c = 0
                l += 2
              else:
                r += 1
                
          if l == m:
            res = map(lambda x: x + 1, list(reversed(fs)) + [y] + ss)
            break
  
  if res:
    print("YES")
    print(" ".join(map(str, res)))
  else:
    print("NO")