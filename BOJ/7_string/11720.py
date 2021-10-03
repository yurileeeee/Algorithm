# BOJ 11720 숫자의 합
# https://www.acmicpc.net/problem/11720

n = int(input())
num_list = list(input())
total = 0

for i in num_list:
  total += int(i)

print(total)