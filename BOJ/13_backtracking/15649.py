# BOJ 15649 N과 M (1)
# https://www.acmicpc.net/problem/15649

n, m = map(int, input().split())

check = []
def func():
  if len(check) == m:
    print(' '.join(map(str, check)))
    return
  
  for i in range(1, n+1):
    if i in check:
      continue
    check.append(i)
    func()
    check.pop()

func()