# 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    cnt = [0, 0, 0]   # 각자 정답을 맞춘 개수 
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == num1[(i % 5)]: # num1의 길이만큼 나눠줌 -> 영역 밖까지 반복
            cnt[0] += 1
        if answers[i] == num2[(i % 8)]:
            cnt[1] += 1
        if answers[i] == num3[(i % 10)]:
            cnt[2] += 1
    
    for i in range(3):
        if cnt[i] == max(cnt):  # 가장 많이 맞춘 사람 찾기
            answer.append(i+1)
            
    return answer