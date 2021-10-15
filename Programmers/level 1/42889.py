# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    result = {}
    num = len(stages)

    for stage in range(1, N+1):
        if num != 0:
            count = stages.count(stage) # 각 스테이지의 단계별 실패자 count
            result[stage] = count / num # 실패율 계산
            num -= count
        else:
            result[stage] = 0

    return sorted(result, key=lambda x : result[x], reverse=True)