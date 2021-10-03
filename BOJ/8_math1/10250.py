# BOJ 10250 ACM호텔
# https://www.acmicpc.net/problem/10250

for _ in range(int(input())): # 테스트케이스 개수만큼 실행
  h, w, n = map(int, input().split()) # h: 층수, w: 방수, n: n번째 손님
  floor = n%h         # 층번호
  hotel_num = n//h+1  # 방번호

  if floor == 0 :
    floor = h
    hotel_num -= 1
  print(floor*100 + hotel_num)