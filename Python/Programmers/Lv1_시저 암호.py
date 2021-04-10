# [프로그래머스 Lv1/Python] 시저 암호
# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    low = 'abcdefghijklmnopqrstuvwxyz'
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    for letter in s:
        if letter in low:
            answer+=low[(low.index(letter)+n)%len(low)]
        elif letter in up:
            answer+=up[(up.index(letter)+n)%len(up)]
        else: answer+=" "
    return answer