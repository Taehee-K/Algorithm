# [정올 566/Python] 배열2 - 자가진단3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=203&sca=10a0

n = int(input()) # 자연수 입력받기
num = [100, n] # 첫 번째 항 100, 두 번째 항 입력값으로 초기화

i = 1
while(num[-1]>=0): # 마지막 항이 음수가 아닐 때 반복
    last = num[i-1]-num[i] # 전 항에서 전전항을 뺀 값
    num.append(last)
    i+=1

for i in range(len(num)):
    print(num[i], end = " ")