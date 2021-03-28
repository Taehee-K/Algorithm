# [정올 151/Python] 배열1 - 형성평가2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=51&sca=1090

# 5개의 정수를 입력
num = list(map(int, input().split()))

# 첫 번째 세 번째 다섯 번째 입력받은 정수의 합을 출력
total = 0
for i in range(1, len(num)+1):
    if i==1 or i==3 or i==5:
        total += num[i-1]

print(total)