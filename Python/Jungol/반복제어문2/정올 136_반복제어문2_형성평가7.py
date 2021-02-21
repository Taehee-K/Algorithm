# [정올 136/Python] 반복제어문2 - 형성평가7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=36&sca=1070

# 한 개의 자연수를 입력받아 그 수의 배수를 차례로 10개 출력
n = int(input())

for i in range(10):
    print(n*(i+1), end=" ")