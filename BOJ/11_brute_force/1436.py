# BOJ 1436 영화감독 숌
# https://www.acmicpc.net/problem/1436

n = int(input())
cnt = 0
six = 666

while True:
  if '666' in str(six):
    cnt += 1
  if cnt == n:
    print(six)
    break
  six += 1