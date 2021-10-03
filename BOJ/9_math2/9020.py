# BOJ 9020 골드바흐의 추측
# https://www.acmicpc.net/problem/9020

def Goldbach():
    check = [False, False] + [True] * 10000 #0,1인덱스 false이고 나머지가 true인 길이 10002인 리스트
    
    for i in range(2, 101): # 입력값이 10000까지이므로 100보다 작은 소수의 배수를
        if check[i] == True:
            for j in range(i + i, 10001, i): # false로 바꿔줌 
                check[j] = False

    T = int(input())
    for _ in range(T):
        n = int(input())

        A = n // 2 # 오차가 가장 작아야 하므로 중간부터 조사
        B = A
        for _ in range(10000):
            if check[A] and check[B]:
                print(A, B)
                break
            A -= 1 # 중간값이 소수가 아니면 +-1씩 하며 조사
            B += 1

Goldbach()
