# BOJ 10814 나이순 정렬
# https://www.acmicpc.net/problem/10814

import sys

n = int(sys.stdin.readline())
member = []
for _ in range(n):
  age, name = sys.stdin.readline().split()
  member.append([int(age), name])

member.sort(key=lambda member:(member[0])) #정렬을 목적으로 하는 함수를 값으로 넣음
for i in member:
  print(i[0], i[1])

