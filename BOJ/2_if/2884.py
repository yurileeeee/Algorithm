# BOJ 2884 알람 시계
# https://www.acmicpc.net/problem/2884

hour, minutes = map(int, input().split())

if minutes > 44:
  print(hour, minutes - 45)
elif minutes < 45 and hour > 0:
  print(hour-1, minutes + 15)
else:
  print(23, minutes + 15)