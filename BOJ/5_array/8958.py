# BOJ 8958 OX퀴즈
# https://www.acmicpc.net/problem/8958

# 테스트케이스 개수 입력
num = int(input())

for i in range(num):
  # OX 입력 받음
  test = input()
  # 리스트로 변경
  test_list = list(test)

  total = 0
  temp = 1

  for i in test_list:
    if i == 'O':
      total += temp
      temp += 1
    else:
      temp = 1
  
  print(total)