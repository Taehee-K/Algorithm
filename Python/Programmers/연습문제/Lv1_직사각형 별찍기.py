# [프로그래머스 Lv1/Python] 직사각형 별찍기
# https://programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().strip().split(' '))
[print('*'*a) for _ in range(b)]