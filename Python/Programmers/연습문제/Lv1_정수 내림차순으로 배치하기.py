# [프로그래머스 Lv1/Python] 정수 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    answer = int(''.join(sorted(list(str(n)), reverse = True)))
    return answer