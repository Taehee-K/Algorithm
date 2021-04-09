# [프로그래머스 Lv1/Python] 문자열 내 p와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    # lower() -> 소문자 변경
    # count() -> 'p','y' 개수 연산 후 비교
    if s.lower().count('p') == s.lower().count('y'):  
        return True
    else: return False