# [프로그래머스 Lv1/Python] 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations
def solution(nums):
    prime = []          # 소수 저장할 list
    for three in list(combinations(nums, 3)):   # 주어진 숫자 중 3개로 만들 수 있는 조합
        flag = True                             # 소수인지 나타내줄 flag
        for i in range(2, sum(three)):          # 3개의 수를 더한 값에 대해 소수 체크
            if sum(three)%i==0: flag = False; break;    # 나누어떨어질 때 flag = false
        if flag==True: prime.append(sum(three))         # flag = True일 때 소수 list에 추가
    return len(prime)   # 소수 list의 길이