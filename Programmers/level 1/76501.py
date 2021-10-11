# 음양 더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    for i in range(0, len(signs)):
        if not signs[i]:                    # sign 값이 false 일 때
            absolutes[i] = -absolutes[i]    # absolutes의 값을 음수로 변경해줌
    return sum(absolutes)