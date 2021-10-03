# BOJ 2447 별찍기 - 10
# https://www.acmicpc.net/problem/2447

n = int(input())
# 빈칸으로 채워진 배열을 만들기
stars = [[' ' for _ in range(n)] for _ in range(n)]

# 별이 들어갈 위치에 별을 그려주는 함수
def draw_star(size, x, y):
  if size == 1:
    stars[y][x] = "*"
  else:
    next_size = size // 3
    for dy in range(3):
      for dx in range(3):
        if dy != 1 or dx != 1:
          draw_star(next_size, x+dx*next_size, y+dy*next_size)

draw_star(n, 0, 0)
for k in stars:
  print(''.join(k)) # 합쳐주기