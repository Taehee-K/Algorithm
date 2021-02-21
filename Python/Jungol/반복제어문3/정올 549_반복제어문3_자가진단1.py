# [정올 549/Python] 반복제어문3 - 자가진단1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=186&sca=1080

# 자연수 n을 입력
n = int(input())

# 1부터 홀수를 차례대로 더해나가
total = 0; count = 0; i=1;
while (total<n):
    if i%2==1: 
        total+=i
        count+=1
    i+=1

# 합이 n 이상일 때 더해진 홀수의 개수와 그 합을 출력
print(count, total)