# [코드업 6056/Python] 논리연산 - 참/거짓이 서로 다를 때에만 참 출력하기
# https://codeup.kr/problem.php?id=6056

a, b = map(int, input().split())
print(bool(a) != bool(b))