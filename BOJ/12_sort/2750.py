# BOJ 2750 수 정렬하기
# https://www.acmicpc.net/problem/2750

numbers = []

def sort_li(li): # 버블정렬로 구현
  for i in range(len(li)):
    for j in range(len(li)):
      if li[i] < li[j]:
        li[i], li[j] = li[j], li[i]
  return li

for _ in range(int(input())):
  numbers.append(int(input()))

new_li = sort_li(numbers)
for i in new_li:
  print(i)