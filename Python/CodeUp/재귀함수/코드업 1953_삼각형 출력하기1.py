# [코드업 1953/Python] 재귀함수 - 삼각형 출력하기
# https://codeup.kr/problem.php?id=1953

def Triangle(star):
    print('*'*star)
    if star<n: Triangle(star+1)
    else: return

n = int(input())
Triangle(1)