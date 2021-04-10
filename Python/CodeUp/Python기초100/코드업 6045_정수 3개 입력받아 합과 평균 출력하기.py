# [코드업 6045/Python] 산술연산 - 정수 3개 입력받아 합과 평균 출력하기
# https://codeup.kr/problem.php?id=6045

num = list(map(int, input().split()))
print(sum(num), "%.2f"%(sum(num)/3)) 

