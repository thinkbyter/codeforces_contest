t = int(input())
 
for _ in range(t):
  n = int(input())
  ax = list(map(int, input().split()))
  ma = min(ax)
  mc = ax.count(ma)
  print(n - mc)