# [프로그래머스 Lv1/Python] 탐욕법 - 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    lost = sorted(lost)                                 # 학생 오름차순으로 정렬  
    extra = list(set(lost)-(set(lost)-set(reserve)))    # 잃어버렸는데 여분 있는 학생
    for i in extra: reserve.remove(i); lost.remove(i);  # 여분 있을 시 본인 것 입기
    for i in lost:
        if (i-1) in reserve: reserve.remove(i-1)        # 앞의 사람 체육복 빌리기
        elif (i+1) in reserve: reserve.remove(i+1)      # 뒤의 사람 체육복 빌리기
        else: n-=1                          # 빌릴 사람 없음 -> 체육 못 함
    return n