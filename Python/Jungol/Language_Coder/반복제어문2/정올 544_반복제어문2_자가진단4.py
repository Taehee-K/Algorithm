# [정올 544/Python] 반복제어문2 - 자가진단4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=181&sca=1070

# 100 이하의 정수를 입력
num = int(input())

# 입력받은 정수부터 100까지의 합을 출력
total = 0
for i in range(num, 100+1):
    total+=i
print(total)