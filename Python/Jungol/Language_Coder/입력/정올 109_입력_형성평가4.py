# [정올 109/Python] 입력 - 형성평가4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=9&sca=1020

# 세 개의 정수를 입력받아 합과 평균을 출력
# (단 평균은 소수 이하를 버림하여 정수 부분만 출력한다.)

x, y, z = input().split()
x = int(x);y = int(y); z = int(z);
sum = x+y+z
avg = (x+y+z)//3

print('sum =',sum)
print('avg =',avg)