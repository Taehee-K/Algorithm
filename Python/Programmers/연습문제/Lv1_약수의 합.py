# [프로그래머스 Lv1/Python] 약수의 합
# https://programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    divisor = []                                # 약수 리스트
    if n==0: return 0                           # n = 0일 때 0 리턴
    for i in range(1, int(n**(0.5))+1):         # 1부터 sqrt(n)까지 반복
        if n%i==0:                              # 나누어 떨어지는 divisor일 때
            divisor.append(i)                   # 약수 리스트에 추가
            if i != n//i: divisor.append(n//i)  # sqrt(n)이 아닐 때 약수 짝 추가
    return sum(divisor)                         # 약수 리스트 원소의 합 리턴