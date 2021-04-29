# [프로그래머스 Lv1/Python] 음양 더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    total = 0
    for i in range(len(absolutes)):
        sign = 1 if signs[i]==True else -1
        total+=absolutes[i]*sign
    return total