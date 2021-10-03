# BOJ 3052 나머지
# https://www.acmicpc.net/problem/3052

num_list = []
for i in range(10):
  n = int(input()) # 일단 n을 받아옴 
  num_list.append(n % 42) # n을 42로 나눈 나머지를 리스트에 저장

# set : 집합으로 만들어줌 -> 중복을 허용하지 않는 성질
print(len(set(num_list)))