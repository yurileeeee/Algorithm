# 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = ''
    if len(s) % 2 == 1:
        answer = s[(len(s)-1) // 2]
    else:
        answer = s[(len(s)-1) // 2 : len(s) // 2 + 1]
    return answer