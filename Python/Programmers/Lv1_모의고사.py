# [프로그래머스 Lv1/Python] 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    first = [1,2,3,4,5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    fst = 0; sec = 0; thd = 0;
    for i in range(len(answers)):
        if answers[i]==first[i%len(first)]: fst+=1 
        if answers[i]==second[i%len(second)]: sec+=1 
        if answers[i]==third[i%len(third)]: thd+=1 
    correct = [fst, sec, thd]
    [answer.append(i+1) for i, x in enumerate(correct) if x == max(correct)]
    return answer