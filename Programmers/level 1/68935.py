# 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = ''
    result = 0

    while n > 0:        # 10진법을 뒤집어진 3진법으로 변환
        rest = n % 3
        n //= 3
        answer += str(rest)

    i = 0
    for idx in range(len(answer)-1, -1, -1):    # 3진법을 10진법으로 변환
        result += int(answer[idx]) * (3**i)
        i += 1

    return result


  # 더 간단하게 구현
  # divmod : 몫과 나머지를 반환해줌
  # int(a, b) : a 를 b 진법으로 바꿔서 반환해줌

  # def solution(n):
  # answer = ''

  # while n >= 1:
  #     n, rest = divmod(n, 3)
  #     answer += str(rest)

  # answer = int(answer, 3)

  # return answer
