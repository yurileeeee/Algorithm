# BOJ 11651 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651

import sys

location = []
for _ in range(int(sys.stdin.readline())):
  x, y = map(int, sys.stdin.readline().split())
  location.append([y,x])

spot = sorted(location) # 정렬

for i in range(len(location)):
  print(spot[i][1], spot[i][0])