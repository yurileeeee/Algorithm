# BOJ 3053 택시기하학
# https://www.acmicpc.net/problem/3053

import math

r = int(input())

euclid = r*r*math.pi # 유클리드 기하학
taxi = r*r*2         # 택시 기하학

print('{:.6f}'.format(euclid))
print('{:.6f}'.format(taxi))
