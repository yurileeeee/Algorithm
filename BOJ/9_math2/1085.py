# BOJ 1085 직사각형에서 탈출
# https://www.acmicpc.net/problem/1085

x, y, w, h = map(int, input().split())

top = h - y
bottom = y
left = x
right = w - x

print(min(top, bottom, left, right))