# BOJ 2439 별찍기 -2
# https://www.acmicpc.net/problem/2439

n = int(input())

""" for i in range(1, n+1):
  for j in range(n-i):
    print(" ", end="")
  for j in range(i):
    print("*", end="")
  print("") """

  for i in range(1, n+1):
  print(" "*(n-i) + "*" * i)