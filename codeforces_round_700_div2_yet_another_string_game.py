t = int(input())
 
for _ in range(t):
  ss = list(input())
  # c not s
  for i, s in enumerate(ss):
    if i % 2 == 0: # Alice.
      if s == 'a':
        ss[i] = 'b'
      else:
        ss[i] = 'a'
    else:
      if s == 'z':
        ss[i] = 'y'
      else:
        ss[i] = 'z'
        
  print("".join(ss))
    