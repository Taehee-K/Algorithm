# [프로그래머스 Lv1/Python] 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = [arr[0]] # 첫 번째 원소로 초기화     
    [answer.append(arr[i]) for i in range(1,len(arr)) if arr[i]!=answer[-1]]
    return answer