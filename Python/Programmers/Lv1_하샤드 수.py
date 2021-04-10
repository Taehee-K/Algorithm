# [프로그래머스 Lv1/Python] 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    if x%sum(list(map(int, str(x)))) ==0: return True
    else: return False