# [정올 132/Python] 반복제어문2 - 형성평가3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=32&sca=1070

# 1부터 입력받은 정수까지의 5의 배수의 합을 구하여 출력
n = int(input())

total = 0
for i in range(1, n+1):
    if i%5==0:
        total+= i
print(total)