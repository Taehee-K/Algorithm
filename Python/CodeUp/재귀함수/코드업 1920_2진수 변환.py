# [코드업 1920/Python] 재귀함수 - 2진수 변환
# https://codeup.kr/problem.php?id=1920

def Binary(n):
    num = str(bin(n))   # bin() 통해 이진수로 변환
    print(num[2:])      # 0b 접두사 제거

n = int(input())
Binary(n)