# 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]        # rank 리스트에 등수 저장 
    answer = [0, 0]
    
    zero = lottos.count(0)              # 0으로 추정한 값이 몇개인지 카운트
    cnt = 0                             # 확실히 일치하는 숫자 카운트
    
    
    for i in lottos:
        if i in win_nums:               # 당첨 번호 안에 내 로또 번호가 있는지 검사 후 cnt + 1
                cnt += 1
                
    answer[0] = rank[cnt + zero]        # 최고 순위
    answer[1] = rank[cnt]               # 최저 순위
        
    return answer