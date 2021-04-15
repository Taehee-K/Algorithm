# [코드업 6070/Python] 선택실행구조 - 월 입력받아 계절 출력하기
# https://codeup.kr/problem.php?id=6070

month = int(input())
if month//3==1: print('spring')
elif month//3==2: print('summer')
elif month//3==3: print('fall')
else: print('winter')