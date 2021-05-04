# [프로그래머스 Lv1/Python] 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    # 3진법 으로 n 나타내기
    trinary = ''
    while n>2:
        trinary += str(n%3)
        n = n//3
    trinary += str(n)
    
    decimal = 0
    for i in range(len(trinary)):
        decimal += int(trinary[len(trinary)-i-1])*(3**i)
    return decimal