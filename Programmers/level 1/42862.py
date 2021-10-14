# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve): 
    reser_del = set(reserve)-set(lost) # 중복 제거
    lost_del = set(lost)-set(reserve) # 중복 제거

    for i in reser_del: 
        if i-1 in lost_del: 
            lost_del.remove(i-1) 
        elif i+1 in lost_del: 
            lost_del.remove(i+1) 
        
    return n-len(lost_del)

