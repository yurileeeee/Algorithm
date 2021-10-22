# 두 개 뽑아서 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations

def solution(numbers):
    answer = []
    arr = list(combinations(numbers, 2))
    for i in arr:
        answer.append(i[0] + i[1])
        answer = list(set(answer))  # 중복 제거
    return sorted(answer)