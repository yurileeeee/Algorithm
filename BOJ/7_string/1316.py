# BOJ 1316 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

num = int(input())
cnt = 0

for _ in range(num):
  word = input()
  for i in range(len(word)-1):    # i+1까지 확인하므로 단어 길이보다 -1 해줌
    if word[i] != word[i+1]:      # i와 i+1의 단어가 다른데
      if word[i] in word[i+1:]:   # i가 i+1 이후의 단어에 포함되어 있다면?
        num -= 1                  # 그룹이 아님
        break
print(num)

