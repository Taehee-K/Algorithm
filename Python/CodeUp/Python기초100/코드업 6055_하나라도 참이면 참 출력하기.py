# [코드업 6055/Python] 논리연산 - 하나라도 참이면 참 출력하기
# https://codeup.kr/problem.php?id=6055

a, b = map(int, input().split())
print(bool(a) or bool(b))