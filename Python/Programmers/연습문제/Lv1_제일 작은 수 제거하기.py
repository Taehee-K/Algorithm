# [프로그래머스 Lv1/Python] 제일 작은 수 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    if len(arr)>1: 
        del arr[arr.index(min(arr))]
        return arr
    else: return [-1]