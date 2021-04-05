# [프로그래머스 Lv1/Python] 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128?language=python3

def solution(a, b):
    answer = 0
    for i in range(len(a)):    # a, b 길이 같음
        answer += a[i]*b[i]    # 각 인덱스별 원소 곱한 값 더해 내적 구함
    return answer