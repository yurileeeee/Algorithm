# 문자열 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    answer = ''
    arr = list(s)
    arr.sort(reverse=True)
        
    for i in arr:
        answer += i
    return answer