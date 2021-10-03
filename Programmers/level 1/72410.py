# 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    # 1 : 소문자 변경
    new_id = new_id.lower()

    # 2 : 영어 소문자, 숫자, -, _, . 만 answer에 추가
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c

    # 3 : .. 두번 연속된 경우 . 하나로 replace
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4 : 맨 처음, 맨 뒤에 .이 있는 경우 제거
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]

    # 5 : 공백인 경우 a 로 채워줌
    if answer == '':
        answer = 'a'

    # 6 : 문자열 길이가 15 이상일 경우 cut, 마지막 문자열 . 제거
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7 : 문자열 길이가 3 이하일 경우 마지막 문자열 반복
    while len(answer) < 3:
        answer += answer[-1]
    return answer