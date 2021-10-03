# BOJ 4344 평균은 넘겠지
# https://www.acmicpc.net/problem/4344

num = int(input())

for i in range(num):
  test = list(map(int, input().split()))
  student = test[0]
  score = test[1:]
  avg = sum(score) / student

  cnt = 0
  for i in score:
    if i > avg:
      cnt += 1
    
  percent = cnt / student * 100

  print('{:.3f}%'.format(percent))
