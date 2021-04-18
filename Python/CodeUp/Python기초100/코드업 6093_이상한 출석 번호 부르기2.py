# [코드업 6093/Python] 종합 - 이상한 출석 번호 부르기2
# https://codeup.kr/problem.php?id=6093

n = int(input())                        # 출석 번호 부른 횟수
call = list(map(int, input().split()))  # 무작위로 부른 번호 배열

for i in range(n-1, -1, -1): print(call[i], end = " ")

