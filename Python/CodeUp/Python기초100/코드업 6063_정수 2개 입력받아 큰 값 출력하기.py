# [코드업 6063/Python] 3항연산 - 정수 2개 입력받아 큰 값 출력하기
# https://codeup.kr/problem.php?id=6063

a, b = map(int, input().split())

# 3항 연산: x(True 일 때) if 조건식 else y(false 일 때)
c = a if a>b else b
print(c)