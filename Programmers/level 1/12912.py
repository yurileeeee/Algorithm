# 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    
    if a > b : a, b = b, a
        
    answer = sum(range(a, b+1)) # 합은 sum으로 쓰기 기억!
    return answer