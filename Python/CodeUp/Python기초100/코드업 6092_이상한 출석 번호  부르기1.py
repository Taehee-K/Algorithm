# [코드업 6092/Python] 종합 - 이상한 출석 번호 부르기1
# https://codeup.kr/problem.php?id=6092

n = int(input())                    # 출석 번호 부른 횟수
call = list(map(int, input().split()))    # 무작위로 부른 번호 배열
student = [0]*23

for num in call:
    student[num-1]+=1

for i in student: print(i, end = " ")

