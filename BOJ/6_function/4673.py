# BOJ 4673 셀프 넘버
# https://www.acmicpc.net/problem/4673

natural_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):     # i = 127
  for j in str(i):            # j = 1, 2, 7
    i += int(j)               # i = 127 + 1 + 2 + 7 = 137
  generated_num.add(i)        # generated_num : 생성자로 생긴 수들이 저장됨

# self_num : 생성자가 없는 수 --> natural_num - generated_num
self_num = sorted(natural_num - generated_num)

for i in self_num:
  print(i)