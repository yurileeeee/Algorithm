# BOJ 2908 상수
# https://www.acmicpc.net/problem/2908

a, b = input().split()

reverse_a = a[::-1]
reverse_b = b[::-1]

if reverse_a > reverse_b:
  print(reverse_a)
else:
  print(reverse_b)