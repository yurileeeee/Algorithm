# 폰켓몬
# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    length = len(nums) // 2
    temp = list(set(nums))  # set 을 이용한 중복 제거
    
    for i in temp :
        if(answer < length):
            answer +=1
            
    return answer