# 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    total = 0

    for i in sorted(d):
        if total + i <= budget:   # i를 더했을 때 예산을 넘치는 경우 방지
            total += i
            answer += 1
    return answer