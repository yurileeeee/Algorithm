# BOJ 2751 수 정렬하기 2
# https://www.acmicpc.net/problem/2751

import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')