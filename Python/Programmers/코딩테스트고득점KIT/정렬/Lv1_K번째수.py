# [프로그래머스 Lv1/Python] 정렬 - K번째수
# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        answer.append(sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1])
    return answer

# i,j,k = command 식으로 i,j,k를 따로 입력했으면 코드가 조금 더 가독성 있었을 것 같다