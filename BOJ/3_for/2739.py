# BOJ 2739 구구단
# https://www.acmicpc.net/problem/2739

n = int(input())

for i in range(1,10):
  print('{} * {} = {}'.format(n, i, n*i))