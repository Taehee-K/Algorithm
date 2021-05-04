# [프로그래머스 Lv1/Python] 포켓몬
# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(nums):
    if len(set(nums)) > len(nums)//2:
        return len(nums)//2
    else: return len(set(nums))
    # return min(len(nums)//2, len(set(nums))) 으로도 가능