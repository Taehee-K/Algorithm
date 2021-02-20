# [정올 539/Python] 반복제어문1 - 자가진단4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=176&sca=1060
 
# 정수를 계속 입력
# 100 이상의 수가 입력->마지막 입력된 수를 포함하여 합계와 평균을 출력
# (평균은 반올림하여 소수 첫째자리까지 출력)

num = list(map(int, input().split()))
total = 0
i=0
while(num[i]<100):
    total += num[i]
    i += 1
total+= num[i]
i+=1 
print(total)
print(round(total/i,1))