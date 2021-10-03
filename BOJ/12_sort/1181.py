# BOJ 1181 단어 정렬
# https://www.acmicpc.net/problem/1181

n = int(input())
word = []
sort_word = []

for i in range(n):
  word.append(input())

set_word = list(set(word)) # 중복 제거
for i in set_word:
  sort_word.append([len(i), i]) # [길이, 단어]로 저장

result = sorted(sort_word) # 길이 -> 사전순 정렬
for len_word, word in result:
  print(word)