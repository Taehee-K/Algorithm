# [코드업 6019/Python] 입출력 - 연월일 입력받아 순서 바꿔 출력하기
# https://codeup.kr/problem.php?id=6019

# "연도.월.일" 입력 >> "일-월-연도" 순서로 출력
y, m, d = input().split('.')
print(d, m, y, sep = "-")