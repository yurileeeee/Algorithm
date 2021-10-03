# BOJ 4948 베르트랑 공준
# https://www.acmicpc.net/problem/4948

import math

def isPrime(num):
  if num == 1: return False
  for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0: return False
  return True

li = list(range(2,246912)) # 미리 123456의 2배인 246912
prime_li = []
for i in li:
  if isPrime(i):          # 그 사이의 소수를 구해 prime_li를 만들어 둠
    prime_li.append(i)

while(1):
  answer = 0
  n = int(input())
  if n == 0: break # 입력이 0 이면 끝

  for i in prime_li: # 미리 만들어 둔 prime_li에서
    if n < i <= n*2: # 범위 사이에 i가 있다면 
      answer += 1    # 개수 1개 증가
  
  print(answer)