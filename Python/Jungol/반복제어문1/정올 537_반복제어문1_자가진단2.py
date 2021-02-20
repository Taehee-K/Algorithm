# [정올 537/Python] 반복제어문1 - 자가진단2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=174&sca=1060
 
# 100 이하의 양의 정수 입력
num = int(input())

# while 문을 이용하여 1부터 입력받은 정수까지의 합을 구하여 출력
i = 1
total = 0
while(i<=num):
    total +=i
    i+=1
print(total)
