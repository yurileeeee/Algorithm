# BOJ 1157 단어 공부
# https://www.acmicpc.net/problem/1157

word = input().lower()    # 소문자로 바꿈
set_word = list(set(word)) # 중복된 문자 제거, 리스트로 저장
cnt_list = []

for i in set_word:
  cnt = word.count(i) # 몇번 나오는지 카운트
  cnt_list.append(cnt) # 카운트 리스트에 저장

if cnt_list.count(max(cnt_list)) > 1: # 가장 많이 사용된 알파벳이 여러개인 경우
  print('?')
else:
  max_idx = cnt_list.index(max(cnt_list))
  print(set_word[max_idx].upper()) # 대문자로 출력