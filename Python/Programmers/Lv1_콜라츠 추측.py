# [프로그래머스 Lv1/Python] 콜라츠 추측
# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    count = 0
    while num>1:
        if num%2==0: num = num//2
        else: num = num*3+1
        count+=1
    if count<500: return count
    else: return -1