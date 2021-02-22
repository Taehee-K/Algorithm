# [정올 141/Python] 반복제어문3 - 형성평가2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=41&sca=1080

# 1부터 100까지의 정수 중 한 개를 입력
n = int(input())

# 100 보다 작은 배수들을 차례로 출력
mul=1
while(n*mul<100):
    print(n*mul, end=" ")
    if (n*mul)%10==0:   # 10 의 배수가 출력
        break   # 프로그램 종료
    mul+=1 
