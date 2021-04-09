# [프로그래머스 Lv1/Python] 수박수박수박수박수박수?
# https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    answer = ''
    pattern = '수박'
    for i in range(n): answer+=pattern[i%2]
    return answer