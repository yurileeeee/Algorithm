# BOJ 2675 문자열 반복
# https://www.acmicpc.net/problem/2675

t = int(input())    # 테스트 케이스의 수

for i in range(t):
  r, s = map(str, input().split())    # r: 반복 횟수, s: 문자열
  word = list(s)

  for i in word:
    print(i * int(r), end='') # 각 문자열 * 반복횟수 프린트
  print('')


  """ for i in range(t):
    r, s = input().split()
    result = ''
    for i in s:
      result += int(r) * i
    print(result) """