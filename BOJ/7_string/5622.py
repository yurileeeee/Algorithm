# BOJ 5622 다이얼
# https://www.acmicpc.net/problem/5622

word = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for i in range(len(word)):
  for j in dial:
    if(word[i] in j): # 입력 문자열 중 dial에 해당하는 문자가 있으면
      time += dial.index(j) + 3 # 해당 dial의 인덱스 + 3을 time에 추가함
print(time)

""" word_list = list(word)
num_list = []

for i in word_list:
  if i == 'A' or i == 'B' or i =='C':
    num_list.append(2)
  elif i == 'D' or i == 'E' or i =='F':
    num_list.append(3)
  elif i == 'G' or i == 'H' or i =='I':
    num_list.append(4)
  elif i == 'J' or i == 'K' or i =='L':
    num_list.append(5)
  elif i == 'M' or i == 'N' or i =='O':
    num_list.append(6)
  elif i == 'P' or i == 'Q' or i =='R' or i == 'S':
    num_list.append(7)
  elif i == 'T' or i == 'U' or i =='V':
    num_list.append(8)
  else:
    num_list.append(9)

print(sum(num_list) + len(num_list)) """
