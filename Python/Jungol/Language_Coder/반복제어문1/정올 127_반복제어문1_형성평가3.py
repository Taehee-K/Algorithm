# [정올 127/Python] 반복제어문1 - 형성평가3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=27&sca=1060

# 0 부터 100 까지의 정수를 계속 입력
num = list(map(int, input().split()))

# 범위를 벗어나는 수가 입력
# 그 이전까지 입력된 자료의 합계와 평균을 출력
# (평균은 반올림하여 소수 첫째자리까지 출력)
i = 0
total = 0
while(num[i]>=0 and num[i]<=100):
    total+=num[i]
    i+=1
print("sum :", total)
print("avg :", round(total/i, 1))