# BOJ 2231 분해합
# https://www.acmicpc.net/problem/2231

n = int(input())
result = 0

for i in range(1, n+1):
  numbers = list(map(int, str(i))) # n의 자리수를 리스트로 저장
  result = i + sum(numbers) # 1부터 n까지 분해합을 구함
  if result == n: # n과 같을 경우 i는 n의 생성자
    print(i)
    break
  if i == n: # i와 n이 같을 때까지 결과가 나오지 않으면 
    print(0) # 생성자가 없음을 의미