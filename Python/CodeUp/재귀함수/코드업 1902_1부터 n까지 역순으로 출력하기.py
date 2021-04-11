# [코드업 1902/Python] 재귀함수 - 1부터 n까지 역순으로 출력하기
# https://codeup.kr/problem.php?id=1902

def Number(n):
    print(n)
    if n>1: Number(n-1)

num = int(input())
Number(num)