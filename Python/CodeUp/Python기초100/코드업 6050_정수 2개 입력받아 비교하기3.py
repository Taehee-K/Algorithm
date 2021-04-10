# [코드업 6050/Python] 비교연산 - 정수 2개 입력받아 비교하기3
# https://codeup.kr/problem.php?id=6050

a, b = map(int, input().split())
#작다(<)/크다(>)/다르다(!) 기호는 등호(=)와 함께 왼쪽에 붙여써야 한다
if b>=a: print(True) 
else: print(False)
