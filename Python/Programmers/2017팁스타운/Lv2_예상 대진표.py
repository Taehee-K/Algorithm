# [프로그래머스 Lv2/Python] 예상 대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    count = 0
    while a!=b:
        a = (a+1)//2; b = (b+1)//2
        count+=1
    return count
