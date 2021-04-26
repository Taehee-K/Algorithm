# [프로그래머스 Lv1/Python] 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    strings.sort()  # 알파벳순으로 정렬
    answer = sorted(strings, key = lambda x: x[n]) # 람다 메개변수 통해 search key 지정
    return answer

# lambda 표현식에 익숙해지기!