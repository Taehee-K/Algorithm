# [정올 548/Python] 반복제어문2 - 자가진단8
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=185&sca=1070

for i in range(2, 5):
    for j in range(1, 6):
        print(i,"*",j,"= {:>2}   ".format(i*j), end="")
    print()