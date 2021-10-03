# BOJ 1330 두 수 비교하기
# https://www.acmicpc.net/problem/1330

numA, numB = map(int, input().split())

if numA > numB:
  print('>')
elif numA < numB:
  print('<')
else :
  print('==')