# [코드업 6081/Python] 종합 - 16진수 구구단 출력하기
# https://codeup.kr/problem.php?id=6081

n = int(input(), 16)    #16진수로 입력받기

for i in range(1, 16):
    print('%X'%n, '*%X'%(i), '=%X'%(n*i), sep = '')