# [프로그래머스 Lv2/Python] 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981

from collections import deque   # 스택 사용
def solution(n, words):
    prev = []       # words previously mentioned
    for i in range(len(words)):
        number = n if (i+1)%n==0 else ((i+1)%n) # n번째 사람
        turn = (i//n) +1                        # 차례
        if words[i] not in prev:                # 스택에 없는 단어일 시
            if len(prev)>0 and prev[-1][-1]!=words[i][0]:   # 이전 단어의 마지막 글자와 같은 시작 글자인지 체크
                return [number, turn]                       # 아니라면 탈락
            prev.append(words[i])                           # 맞을 시 스택에 추가
        else: return [number, turn]                         # 스택에 있는 단어 말할 시 탈락
    return [0,0]   # 탈락자 없을 시 [0,0] 리턴
