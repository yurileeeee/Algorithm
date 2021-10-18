# 약수의 개수와 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    cnt = 0                  # 숫자별 약수의 개수 카운트

    for num in range(left, right + 1):
        for i in range(1, num + 1):
            if num % i == 0:
                cnt += 1     # 약수 존재시 cnt + 1
        if cnt % 2 == 0:     # 짝수 개의 약수면 더하기
            answer += num
        elif cnt % 2 == 1:  # 홀수 개의 약수면 빼기
            answer -= num
        cnt = 0             # 다음 숫자를 위해 cnt 는 0으로 리셋
    return answer