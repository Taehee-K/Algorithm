# [코드업 1920/Python] 재귀함수 - 2진수 변환
# https://codeup.kr/problem.php?id=1920

def Binary(n):
    num = str(bin(n))
    print(num[2:])

n = int(input())
Binary(n)