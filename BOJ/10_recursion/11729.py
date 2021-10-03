# BOJ 11729 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729

def hanoi(num, a, b, c):
  if num == 1:
    print(a, c)
  else:
    hanoi(num-1, a, c, b)
    print(a, c)
    hanoi(num-1, b, a, c)

n = int(input())
total = 0

for i in range(n):
  total = total * 2 + 1

print(total)
hanoi(n, 1, 2, 3)
