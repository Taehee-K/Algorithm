# [정올 139/Python] 반복제어문2 - 형성평가A
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=39&sca=1070

# 2부터 9까지의 수 중 2개를 입력
x, y = map(int, input().split())

# 입력받은 수 사이의 구구단을 출력
for i in range(9):
    for j in range(abs(x-y)+1):
        if x>y: 
            print("{} * {} = {:>2}".format(x-j, i+1, (x-j)*(i+1)), end="   ")
        else: 
            print("{} * {} = {:>2}".format(x+j, i+1, (x+j)*(i+1)), end="   ")
    print()