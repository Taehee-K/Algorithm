# [정올 148/Python] 반복제어문3 - 형성평가9
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=48&sca=1080

n = int(input())

for i in range(2*n-1):
    if i<n:
        print("# "*(i+1))
    else: 
        print("  "*(i+1-n)+"# "*(2*n-i-1))

