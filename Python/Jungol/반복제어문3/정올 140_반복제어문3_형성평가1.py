# [정올 140/Python] 반복제어문3 - 형성평가1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=40&sca=1080

# 정수 20 개를 입력받아서 그 합과 평균을 출력
num = list(map(int, input().split()))

# 0 입력->그 때까지 입력된 합과 평균을 출력
total = 0
for i in range(20):
    total +=num[i]
    if num[i]==0:
        print(total, total//(i))
        break
    elif i==19:
        print(total, total//20)

