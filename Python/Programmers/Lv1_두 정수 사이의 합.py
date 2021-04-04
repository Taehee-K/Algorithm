# [프로그래머스 Lv1/Python] 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3

def solution(a, b):
    # a<b 가 되도록 순서 바꿔준다
    if a>b: a, b = b, a

    total = 0
    for i in range(a, b+1): #  a와 b 사이에 속한 모든 정수의 합 구하기
        total+=i
    # sum(range(a, b+1)) 로 sum() 함수 통해 해결 가능

    return total