# BOJ 2869 달팽이는 올라가고 싶다
# https://www.acmicpc.net/problem/2869

import math

a, b, v = map(int, input().split())

# 마지막 날에는 밤에 미끄러지는 시간이 없음을 고려
day = (v-a) / (a-b) + 1
print(math.ceil(day))