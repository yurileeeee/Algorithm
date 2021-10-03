# BOJ 11022 A+B-8
# https://www.acmicpc.net/problem/11022

test = int(input())

for i in range(1, test+1):
  a, b = map(int, input().split())
  print('Case #{}: {} + {} = {}'.format(i, a, b, a+b))