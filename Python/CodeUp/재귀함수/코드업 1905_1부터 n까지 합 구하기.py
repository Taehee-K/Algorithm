# [코드업 1905/Python] 재귀함수 - 1부터 n까지 합 구하기
# https://codeup.kr/problem.php?id=1905

import sys
sys.setrecursionlimit(10**9) # 임의로 재귀호출 횟수를 늘려준다

def Add(n, total):
    total +=n
    if n>0: Add(n-1, total)
    else: print(total)
    
n = int(input())
Add(n, 0)