# [프로그래머스 Lv2/Python] 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973

# 큐 사용한 풀이 
from collections import deque 
def solution(s):
    stack = []  # 문자 하나씩 넣었다 뺄 스택
    for i in s:
        if len(stack)!=0 and stack[-1]==i:  # 직전 문자와 같으면
            stack.pop()                     # 스택에서 제거
        else: stack.append(i)               # 짝지어 제거할 문자 없을 시 스택에 추가
    answer = 1 if len(stack)==0 else 0      # 성공일 시 1, 실패일 시 0 리턴
    return answer


# 원래 제출한 solution(재귀함수 활용) -> 런타임 에러로 시간초과
def solution(s):
    answer = 1 if len(s)==0 else 0
    for i in range(1, len(s)):
        if s[i]==s[i-1]: 
            s = s[:i-1]+s[i+1:]
            return solution(s)
    return answer

