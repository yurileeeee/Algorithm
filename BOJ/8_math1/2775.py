# BOJ 2775 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775

for _ in range(int(input())):
  floor = int(input())
  num = int(input())

  f0 = [x for x in range(1, num+1)] #0층의 인원 수

  for k in range(floor): #층의 개수만큼
    for i in range(1, num): #1~num-1까지
      f0[i] += f0[i-1]
  print(f0[-1]) #가장 마지막 수 출력

    