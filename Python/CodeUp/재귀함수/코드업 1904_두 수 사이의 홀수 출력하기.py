# [코드업 1904/Python] 재귀함수 - 두 수 사이의 홀수 출력하기
# https://codeup.kr/problem.php?id=1904

def Odd(start, end):
    if start%2==1: print(start, end = " ")
    if start<end: Odd(start+1, end)

start, end = map(int, input().split())
Odd(start, end)