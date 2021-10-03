# BOJ 2581 소수
# https://www.acmicpc.net/problem/2581

m = int(input())
n = int(input())
sosu = []

for i in range(m, n+1): # m부터 n까지
  error = 0
  if i > 1:
    for j in range(2, i):
      if i%j == 0:
        error += 1
        break
    if error == 0:
      sosu.append(i)

if len(sosu) > 0:
  print(sum(sosu))
  print(min(sosu))
else:
  print(-1)    
