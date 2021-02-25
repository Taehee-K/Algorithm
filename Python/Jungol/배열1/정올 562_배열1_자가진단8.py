# [정올 562/Python] 배열1 - 자가진단8
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=199&sca=1090

# 10개의 정수 입력받기
num = list(map(int, input().split()))

even = 0; odd=0;
for i in range(1, len(num)+1): 
    if i%2==0: #짝수 번째 입력된 값
        even+=num[i-1]
    else : #홀수 번째 입력된 값
        odd+=num[i-1]

print("sum :", even)
print("avg :", round(odd/5, 1))

