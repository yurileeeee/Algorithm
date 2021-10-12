# 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)   # collections를 사용해 개수 세기
    return list(answer.keys())[0]