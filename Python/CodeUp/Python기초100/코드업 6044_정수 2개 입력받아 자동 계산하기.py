# [코드업 6044/Python] 산술연산 - 정수 2개 입력받아 자동 계산하기
# https://codeup.kr/problem.php?id=6044

a, b = map(int, input().split())
print(a+b)  #합
print(a-b)  #차
print(a*b)  #곱
print(a//b) #몫
print(a%b)  #나머지
print('%.2f' %(a/b))   #나눈 값
