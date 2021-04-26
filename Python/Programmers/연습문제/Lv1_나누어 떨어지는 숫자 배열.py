# [프로그래머스 Lv1/Python] 나누어 떨어지는 숫자 배열
# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    for num in arr: 
        if num%divisor==0: answer.append(num)
    if len(answer)==0: answer.append(-1)
    answer.sort()
    return answer