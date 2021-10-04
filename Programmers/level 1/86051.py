# 없는 숫자 더하기
# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    answer = 0
    check = [0] * 10
    
    for i in numbers :      # 0 ~ 9 중 존재하는 숫자에 1 표시
        check[i] += 1
    for i in check :
        if i == 0 :        
            answer += check.index(i)     # 0으로 표시된 숫자들의 인덱스를 더함
            check[check.index(i)] = 1    # 이미 더한 숫자의 인덱스는 1로 바꿈
    return answer