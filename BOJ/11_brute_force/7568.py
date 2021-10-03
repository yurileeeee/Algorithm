# BOJ 7568 덩치
# https://www.acmicpc.net/problem/7568

li = []

for _ in range(int(input())):
  weight, height = map(int, input().split())
  li.append((weight, height))

for i in li:
  rank = 1 # k+1 만큼의 등수이므로 처음 rank = 1
  for j in li:
    if i[0] < j[0] and i[1] < j[1]: # 몸무게와 키 모두 작을 경우 
      rank += 1                     # rank + 1
  print(rank, end = " ")
  