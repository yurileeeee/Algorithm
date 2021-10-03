# BOJ 1110 더하기 사이클
# https://www.acmicpc.net/problem/1110

n = int(input())
store = n     # 현재 n 값 저장
new_num = 0   # 새로운 n 값 저장
plus = 0      # 자릿수 합 저장
count = 0     # 사이클 카운트

while True:
  plus = n//10 + n%10
  new_num = (n%10)*10 + plus%10   # plus%10 : plus의 일의 자리
  count += 1
  n = new_num       # n에 new_num 저장 후 반복
  if new_num == store:
    break
print(count)
