# BOJ 11653 소인수분해
# https://www.acmicpc.net/problem/11653

n = int(input())

i = 2             
while n != 1:       # 끝까지 나눈 후인 1이 될 때까지
  if n % i == 0:    # n을 i로 나눈 나머지가 0일 때
    n = n // i      # n은 몫이 됨
    print(i)
  else : 
    i += 1          # 나눠지지 않을 때는 i+1