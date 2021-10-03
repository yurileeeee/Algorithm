# BOJ 18870 좌표 압축
# https://www.acmicpc.net/problem/18870

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr2 = list(sorted(set(arr)))
dic = {value: index for index, value in enumerate(arr2)}

for element in arr:
    print(dic[element], end= " ")