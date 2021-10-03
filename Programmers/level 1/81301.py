# 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = s
    # 글자와 숫자를 이어주는 딕셔너리
    words = {'zero': '0', 'one': '1', 'two': '2', 
              'three': '3', 'four': '4', 'five': '5', 
              'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    for key, value in words.items():
        answer = answer.replace(key, value) # words 의 key가 answer에 존재하는 경우 value로 교체해줌
    return int(answer)