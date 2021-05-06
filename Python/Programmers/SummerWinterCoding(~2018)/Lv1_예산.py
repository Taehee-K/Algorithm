# [프로그래머스 Lv1/Python] 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    tot = sorted(d)           # 부서별 신청 금액 오름차순 정렬
    while sum(tot)>budget:    # 부서별 신청 금액의 합 > budget일 때 반복
        tot.remove(tot[-1])   # 신청 금액이 큰 부서 제거
    return len(tot)

# 시간초과 오류
from itertools import combinations
def solution(d, budget):
    for i in range(len(d), 0, -1):              # 지원할 부서 개수
        for tot in list(combinations(d, i)):    # 가능한 조합들
            if sum(tot)<=budget: return i       # 조합의 합 < 예산일 시 부서 개수 리턴
    return 0    # 지원 가능한 부서가 없을 때