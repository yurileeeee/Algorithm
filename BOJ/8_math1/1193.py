# BOJ 1193 분수찾기
# https://www.acmicpc.net/problem/1193

n = int(input())
line = 1

while n > line:   # n = 14일 때
  n -= line       # n = 13, 11, 8, 4, 
  line += 1       # line = 2, 3, 4, 5

if line%2 == 0:
  i = n
  j = line - n + 1
else:
  i = line - n + 1
  j = n

print('{}/{}'.format(i, j)) # 분자/분모