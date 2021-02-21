# [정올 543/Python] 반복제어문2 - 자가진단3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=180&sca=1070

# 정수를 입력
num = int(input())

# 1부터 입력받은 정수까지의 짝수를 차례대로 출력
for i in range(1,num+1):
    if i%2==0:
        print(i, end=" ")