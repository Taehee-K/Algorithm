# [정올 515/Python] 입력 - 자가진단7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=152&sca=1020

# 두 개의 정수 입력 받으면 곱과 몫 출력하기
x, y = input().split()
mul = int(x)*int(y)
div = int(x)//int(y)

print(x,'*',y,'=',mul)
print(x,'/',y,'=',div)