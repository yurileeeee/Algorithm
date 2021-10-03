# BOJ 1065 한수
# https://www.acmicpc.net/problem/1065

n = int(input())
hansu = 0

for i in range(1, n+1):
  if i < 100:
    hansu += 1    # 1~99까지는 모든 수가 한수임
  else:
    num_list = list(map(int, str(i)))  # i = 123, num_list = [1, 2, 3]
    if num_list[2] - num_list[1] == num_list[1] - num_list[0]:
      hansu += 1
print(hansu)

