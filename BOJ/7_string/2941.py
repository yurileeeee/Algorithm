# BOJ 2941 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
  word = word.replace(i, '*')  # 크로아티아 문자가 있을시 *로 바꿈
print(len(word))
