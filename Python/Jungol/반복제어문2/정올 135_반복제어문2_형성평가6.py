# [정올 135/Python] 반복제어문2 - 형성평가6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=35&sca=1070

# 두 개의 정수 입력
x, y = map(int, input().split())

# 두 정수 사이에 3의 배수이거나 5의 배수인 수들의 합과 평균을 출력
if x<y: start=x;fin=y+1
else: start=y; fin=x+1

total=0; count=0;
for i in range(start, fin):
    if i%3==0 or i%5==0:
        total+=i
        count+=1
print("sum : %d"%(total))
print("avg : {:.1f}".format(total/count))