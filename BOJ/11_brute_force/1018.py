# BOJ 1018 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018

n, m = map(int, input().split())
state = []
board = []
for _ in range(n):
  state.append(input())

for i in range(n-7): # 8행
  for j in range(m-7): # 8열
    idx1 = 0 # 값을 초기화
    idx2 = 0 # 값을 초기화
    for k in range (i, i+8):
      for s in range(j, j+8):
        if(k+s)%2 == 0: # 짝수일때, 홀수일때 색이 같음
          if state[k][s] != 'W': idx1 += 1
          if state[k][s] != 'B': idx2 += 1
        else:
          if state[k][s] != 'B': idx1 += 1
          if state[k][s] != 'W': idx2 += 1
    board.append(idx1)
    board.append(idx2)

print(min(board))