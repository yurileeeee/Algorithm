# BOJ 11650 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

import sys

location = []
for _ in range(int(sys.stdin.readline())):
  x, y = map(int, sys.stdin.readline().split())
  location.append([x,y])

spot = sorted(location) # 정렬

for i in range(len(location)):
  print(spot[i][0], spot[i][1])
