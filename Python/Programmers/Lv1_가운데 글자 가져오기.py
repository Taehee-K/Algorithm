# [프로그래머스 Lv1/Python] 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3

def solution(s):
    answer = ''         # 답 저장할 빈 문자열
    if len(s)%2 == 0:   # 단어의 길이가 짝수
        answer = s[len(s)//2-1:len(s)//2+1]  # 가운데 두 글자 가져오기
    else:               # 단어의 길이가 홀수
        answer = s[len(s)//2] # 가운데 글자 
    return answer       