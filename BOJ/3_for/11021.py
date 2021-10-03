# BOJ 11021 A+B-7
# https://www.acmicpc.net/problem/11021

test = int(input())

for i in range(1, test+1):
  a, b = map(int, input().split())
  print('Case #{}: {}'.format(i, a+b))