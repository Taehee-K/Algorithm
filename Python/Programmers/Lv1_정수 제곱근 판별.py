# [프로그래머스 Lv1/Python] 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    import math
    if math.sqrt(n)%1==0:               # 제곱일 때 
        answer = (math.sqrt(n)+1)**2    # x+1의 제곱 
    else: answer = -1
    return answer