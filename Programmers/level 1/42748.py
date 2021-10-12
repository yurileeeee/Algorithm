# k번째 수
# https://programmers.co.kr/learn/courses/30/lessons/42748

def findK(arr, i, j, k):
    arr = arr[i-1:j]    # i번째부터 j번째까지 자름
    arr.sort()          # 오름차순 정렬
    return arr[k-1]     # k번째 수 리턴

def solution(array, commands):
    answer = []
    for arr in commands:
        i = arr[0]
        j = arr[1]
        k = arr[2]
        answer.append(findK(array, i, j, k))  # 각 commands 에서 나온 k번째 수를 answer에 추가
    return answer

# 더 간단한 풀이
# def solution(array, commands):
#     answer = []
#     for arr in commands:
#         i, j, k = arr
#         answer.append(list(sorted(array[i-1:j]))[k-1])
#     return answer