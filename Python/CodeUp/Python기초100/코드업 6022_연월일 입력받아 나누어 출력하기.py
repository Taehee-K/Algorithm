# [코드업 6022/Python] 입출력 - 연월일 입력받아 나누어 출력하기
# https://codeup.kr/problem.php?id=6022

# 입력: 6자리 연월일(YYMMDD)
# 출력: YY MM DD
s = input()
for i in range(len(s)):
    print(s[i*2:i*2+2], end = " ")