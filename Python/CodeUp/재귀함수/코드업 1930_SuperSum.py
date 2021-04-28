# [코드업 1930/Python] 재귀함수 - SuperSum
# https://codeup.kr/problem.php?id=1930

# 메모리 에러 -> 재귀함수로 다 돌리지 말고 배열 활용해보기
def SuperSum(k, n):
    if k==0: return n
    sum = 0
    for i in range(1, n+1):
        sum+=SuperSum(k-1, i)
    return sum

# sys 통해 예외 처리
import sys
lines = sys.stdin.readlines()
for line in lines:
        k, n = map(int, line.split())
        print(SuperSum(k, n))

# try - exccept 통해 예외처리
while True:
    try: 
        k, n = map(int, input().split())
        print(SuperSum(k, n))
    except EOFError: break