# [코드업 6054/Python] 논리연산 - 둘 다 참일 경우만 참 출력하기
# https://codeup.kr/problem.php?id=6054

a, b = map(int, input().split())
print(bool(a) and bool(b))