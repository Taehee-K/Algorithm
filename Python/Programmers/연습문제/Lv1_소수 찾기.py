# [프로그래머스 Lv1/Python] 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    if n<4: return n-1              # 2, 3 prime number
    
    # 에라토스테네스의 체
    sieve = [1]*(n)                 # 초기화: n개 요소 1로 (소수로 가정)
    for i in range(2, n//2+1):      # i = n//2+1까지 검사
        if sieve[i-1]==1:         
            for j in range(i+i, n+1, i):    # i 이후의 i 배수들
                sieve[j-1] = 0              # False 판정
    return sum(sieve)-1                     # 1은 소수가 아니므로 제외


# 시간초과 오류
def solution(n):
    if n<4: return n-1                          # 2, 3 모두 소수
    prime = 2                                   # 소수 개수
    for num in range(4, n+1):                   # 4부터 n 까지의 수에 대해 
        flag = True                             # 소수인지 알려주는 flag
        for i in range(2, num//2+1):            # 2부터 num//2까지의 수로 나눌 때
            if num%i==0: flag = False; break;   # 나누어 떨어질 때 -> 소수 X
        if flag ==True : prime+=1               # 나누어 떨어지지 않을 때 -> 소수
    return prime