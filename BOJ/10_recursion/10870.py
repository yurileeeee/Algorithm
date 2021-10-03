# BOJ 10870 피보나치 수 5
# https://www.acmicpc.net/problem/10870

n = int(input())

def fibonacci(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(n))