# [프로그래머스 Lv1/Python] 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    if len(s)!=4: return False
    for x in s: 
        if x.isalpha(): return False
    return True