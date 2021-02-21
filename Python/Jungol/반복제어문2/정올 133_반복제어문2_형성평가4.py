# [정올 133/Python] 반복제어문2 - 형성평가4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=33&sca=1070

# n개의 정수를 입력받아 평균을 출력
n = int(input())
num = list(map(int, input().split()))

total = 0
for i in range(n):
    total += num[i]
print("{:.2f}".format(total/n))