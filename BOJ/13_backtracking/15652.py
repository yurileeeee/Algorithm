# BOJ 15652 N과 M (4)
# https://www.acmicpc.net/problem/15652

n, m = map(int, input().split())

check = []
def func(depth, idx, n, m):
  if depth == m:
    print(' '.join(map(str, check)))
    return
  
  for i in range(idx, n):
    check.append(i+1)
    func(depth+1, i, n, m)
    check.pop()

func(0,0,n,m)