# BOJ 2577 숫자의 개수
# https://www.acmicpc.net/problem/2577

numA = int(input())
numB = int(input())
numC = int(input())
result = list(str(numA * numB * numC))

for i in range(10):
  print(result.count(str(i)))