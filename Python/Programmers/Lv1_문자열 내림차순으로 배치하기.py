# [프로그래머스 Lv1/Python] 문자열 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    answer = ''
    lower = []; upper = []
    for letter in s:
        if letter.islower(): lower.append(letter)
        elif letter.isupper(): upper.append(letter)
    answer = ''.join(map(str, sorted(lower, reverse = True)+sorted(upper, reverse = True)))
    return answer