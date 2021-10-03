# BOJ 4153 직각삼각형
# https://www.acmicpc.net/problem/4153

while True:
  numbers = list(map(int, input().split()))
  max_num = max(numbers) # 입력된 수 중 가장 큰 수
  
  if sum(numbers) == 0:
    break

  numbers.remove(max_num)
  if max_num**2 == numbers[0]**2 + numbers[1]**2:
    print('right')
  else:
    print('wrong')