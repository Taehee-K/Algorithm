# [프로그래머스 Lv1/Python] 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = []
    words = s.split(' ')
    for word in words:  
        w = ""
        for i in range(len(word)):
            if i%2==0: w+=word[i].upper()
            else: w+=word[i].lower()
        answer.append(w)
    return " ".join(answer)

# 공백이 여러 개일 경우 때문에 spit(" ")로 구분자 지정

