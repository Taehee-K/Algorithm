# [정올 518/Python] 연산자 - 자가진단1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=155&sca=1030

# 세 개의 정수를 입력 받아서 합계와 평균을 출력
# (단 평균은 소수 이하를 버리고 정수부분만 출력)


num = input().split()

sum = 0
for i in range(3):
    num[i] = int(num[i])
    sum = sum+num[i]

avg = sum//3

print("sum :",sum)
print("avg :",avg)

