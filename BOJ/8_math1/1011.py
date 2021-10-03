# BOJ 1011 Fly me to the Alpha Centauri
# https://www.acmicpc.net/problem/1011

for _ in range(int(input())):
  x, y = map(int, input().split())
  distance = y - x
  move = 1          # 이동최대거리, count별 빈도수
  count = 0         # 이동 횟수
  total_move = 0    # 총 이동거리

  while total_move < distance:
    count += 1
    total_move += move  # count 수에 해당하는 move를 더함
    if count % 2 == 0:  # count가 2의 배수일 때
      move += 1         # move + 1
  print(count)