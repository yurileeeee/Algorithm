# BOJ 15650 N과 M (2)
# https://www.acmicpc.net/problem/15650

n, m = map(int, input().split())
visited = [False]*n
out = []
def func(depth, idx, n, m):
  if depth == m:
    print(' '.join(map(str, out)))
    return
  
  for i in range(idx, n):
    if not visited[i]:
      visited[i] = True
      out.append(i+1)
      func(depth+1, i+1, n, m)
      visited[i] = False
      out.pop()

func(0,0,n,m)