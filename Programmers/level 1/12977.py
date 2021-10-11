# 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations

def isSosu(a, b, c):
    num = a + b + c
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    result = 0
    comb = list(combinations(nums, 3))
    for i in comb:
        if isSosu(i[0], i[1], i[2]):
            result += 1
    return result
