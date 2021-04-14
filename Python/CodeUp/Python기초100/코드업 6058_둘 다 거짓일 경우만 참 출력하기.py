# [코드업 6058/Python] 논리연산 - 둘 다 거짓일 경우만 참 출력하기
# https://codeup.kr/problem.php?id=6058

a, b = map(int, input().split())
print(bool(a)==False and bool(b)==False)