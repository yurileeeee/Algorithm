# BOJ 9663 N-Queen
# https://www.acmicpc.net/problem/9663

import sys

n = int(sys.stdin.readline())

def dfs(arr):
    global ans
    length = len(arr)
    if length==n:
        ans+=1
        return
    candidate = list(range(n)) # 후보가 될 수 있는 자리를 0부터 n-1까지 만들고 제외하는 방법을 사용
    for i in range(length):
        if arr[i] in candidate:  # 같은 가로줄에 있으면 후보에서 제외
            candidate.remove(arr[i])
        distance = length - i
        if arr[i] + distance in candidate:  # 같은 '/' 대각선에 있으면 후보에서 제외
            candidate.remove(arr[i] + distance)
        if arr[i] - distance in candidate:  # 같은 '\' 대각선에 있으면 후보에서 제외
            candidate.remove(arr[i] - distance)
    if candidate:
        for i in candidate:
            arr.append(i)
            dfs(arr)
            arr.pop()
    else:
        return

ans = 0
for i in range(n):
    dfs([i])
print(ans)