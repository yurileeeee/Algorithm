# BOJ 10989 수 정렬하기 3
# https://www.acmicpc.net/problem/10989

import sys 

n = int(input()) 
check_list = [0] * 10001 
for i in range(n): 
  input_num = int(sys.stdin.readline()) 
  check_list[input_num] = check_list[input_num] + 1 
  
for i in range(10001): 
  if check_list[i] != 0: 
    for j in range(check_list[i]): 
      print(i)

