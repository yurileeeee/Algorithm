# BOJ 15552 빠른 A+B
# https://www.acmicpc.net/problem/15552

import sys

test = int(sys.stdin.readline())

for i in range(test):
  a, b = map(int, sys.stdin.readline().split())
  print(a+b)