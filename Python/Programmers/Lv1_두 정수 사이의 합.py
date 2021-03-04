# [프로그래머스 Lv1/Python] 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3

def solution(a, b):
    if a>b: # a<b 가 되도록 순서 바꿔준다
        temp = a
        a = b
        b = temp
    total = 0
    for i in range(a, b+1):
        total+=i

    return total