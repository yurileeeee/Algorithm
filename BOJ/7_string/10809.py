# BOJ 10809 알파벳 찾기
# https://www.acmicpc.net/problem/10809

word = input()
alphabet = list(range(97, 123))  # 아스키 코드 범위

for i in alphabet:
  print(word.find(chr(i)))

# find : 문자열 중 특정 문자를 찾고 위치를 반환해줌. 없을 경우 -1 리턴