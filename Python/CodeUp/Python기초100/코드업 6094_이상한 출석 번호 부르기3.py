# [코드업 6094/Python] 종합 - 이상한 출석 번호 부르기3
# https://codeup.kr/problem.php?id=6094

n = int(input())                        # 출석 번호 부른 횟수
call = list(map(int, input().split()))  # 무작위로 부른 번호 배열

print(min(call))

