# [프로그래머스 Lv1/Python] 2016년
# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    year = {0:0, 1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31} # 2016년 각 달의 일수 dict
    day = 0
    for i in range(a):  # 0월~a-1 달까지의 일수 더하기
        day +=year[i]
    day+=b              # 2016년 1월 1일 부터 지난 날 계산
    week = {0: "THU", 1:"FRI", 2:"SAT", 3:"SUN", 4:"MON", 5:"TUE", 6:"WED"}
    return week[day%7]  