# [정올 128/Python] 반복제어문1 - 형성평가4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=28&sca=1060

# 0 이 입력될 때까지 정수를 계속 입력
num = list(map(int, input().split()))

# 3의 배수와 5의 배수를 제외한 수들의 개수를 출력
count = 0
i=0
while(num[i]!=0):
    if num[i]%3!=0 and num[i]%5!=0 :
        count+=1
    i+=1
print(count)