# [정올 112/Python] 연산자 - 형성평가2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=12&sca=1030

# 두 정수 입력받기
x, y = map(int, input().split())

#몫
div = x//y
#나머지
rem = x%y

print(x,"/",y,"=",str(div)+"..."+str(rem))