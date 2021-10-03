# BOJ 2839 설탕 배달
# https://www.acmicpc.net/problem/2839

sugar = int(input())      # 설탕 무게
bag = 0                   # 봉지 수

while sugar >= 0:
  if sugar % 5 == 0:      # 설탕이 5kg으로 나누어 떨어지면
    bag += (sugar // 5)   # 봉지 + 몫
    print(bag)
    break
  sugar -= 3              # 5kg으로 나누어 떨어질 때까지 3kg을 뺌
  bag += 1                # 3kg 한봉지씩 추가 
else:
  print(-1)               # while문이 거짓으로 판명될 경우 -1