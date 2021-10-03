# BOJ 1712 손익분기점
# https://www.acmicpc.net/problem/1712

a, b, c = map(int, input().split())

if b >= c:              # 가변비용 >= 수입 일 경우 생산대수가 아무리 많아도 적자
  print(-1)
else:
  print((a//(c-b))+1)   # 고정비용 // (수입 - 가변비용) + 1
