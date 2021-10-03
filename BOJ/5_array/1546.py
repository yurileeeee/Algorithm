# BOJ 1546 평균
# https://www.acmicpc.net/problem/1546

# 과목 개수, 과목 점수 입력
num = int(input())
score_list = list(map(int, input().split()))

# 본인 점수 중 최댓값 M
M = max(score_list)

# 새로운 점수 리스트에 저장
new_score = []
for i in range(len(score_list)):
  new_score.append(score_list[i] / M * 100)
  
print(sum(new_score) / num)