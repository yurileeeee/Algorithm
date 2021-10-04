# 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    posL = 10   # 현재 왼손 위치
    posR = 12   # 현재 오른손 위치

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            posL = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            posR = i
        else:   # 2, 5, 8, 0 일 경우
            i = 11 if i == 0 else  i   # 0 일 경우 i = 11 로 지정
            
            # 현재 위치에서 눌러야 할 번호까지의 절댓값 구하기
            absL = abs(i - posL)
            absR = abs(i - posR)
            
            # abs 값을 3으로 나눈 몫과 나머지를 더한 값을 비교
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer+='R'
                posR = i
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer +='L'
                posL = i
            else:   # 양 손에서의 거리가 동일한 경우 hand 값에 따라 결정
                if hand == 'left':
                    answer+='L'
                    posL = i
                else:
                    answer+='R'
                    posR = i
    return answer