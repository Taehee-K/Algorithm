# [프로그래머스 Lv1/Python] 해시 - 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter
def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    if set(participant) == set(completion): # 동명이인이 있을 때
        for name in list(p.keys()):
            if p[name] != c[name]: return name
    else:                                   # 동명이인이 없을 때
        for name in list(p.keys()):
            if name not in c.keys():
                return name


# 시간초과 
def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    if set(participant) == set(completion): # 동명이인이 있을 때
        for name in list(p.keys()):
            if p[name] != c[name]: return name
    else:   # 동명이인이 없을 때
            # 여기서의 for 문 때문에 시간초과 생긴 것으로 보임
        name = [name for name in participant if name not in completion] 
        return name[0]
        
