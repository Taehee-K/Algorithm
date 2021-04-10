# [프로그래머스 Lv1/Python] 자릿수 더하기
# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    return sum(map(int,list(str(n))))