# Contest: https://codeforces.com/contest/1487
# Problem: https://codeforces.com/contest/1487/problem/A
# Attempts: 1
# Solved: during contest

t = int(input())
 
for _ in range(t):
  n = int(input())
  ax = list(map(int, input().split()))
  ma = min(ax)
  mc = ax.count(ma)
  print(n - mc)