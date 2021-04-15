# [코드업 6064/Python] 3항연산 - 정수 3개 입력받아 가장 작은 값 출력하기
# https://codeup.kr/problem.php?id=6064

a, b, c = map(int, input().split())

# 3항 연산: x(True 일 때) if 조건식 else y(false 일 때)
c = (a if a<b else b) if (a if a<b else b)<c else c
print(c)