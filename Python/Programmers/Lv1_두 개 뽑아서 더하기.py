# [프로그래머스 Lv1/Python] 두 개 뽑아서 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3

def solution(numbers):
    answer = [] # answer 담을 list
    for i in range(len(numbers)):   # numbers 배열의 인덱스 하나씩 돌아가며 탐색
        for j in range(i):          # 서로 다른 인덱스 선택
                new = numbers[i]+numbers[j] # 다른 인덱스에 있는 두 개의 수를 뽑아 더하기
                if new not in answer:       # 이미 있는 값이 아니라면
                    answer.append(new)      # answer 배열에 append
    answer.sort()   # 결과 오름차순 정렬
    return answer   