# BOJ 15651 N과 M (3)
# https://www.acmicpc.net/problem/15651

n, m = map(int, input().split())

check = []
def func():
  if len(check) == m:
    print(' '.join(map(str, check)))
    return
  
  for i in range(1, n+1):
    check.append(i)
    func()
    check.pop()

func()