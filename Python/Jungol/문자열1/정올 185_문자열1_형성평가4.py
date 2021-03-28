# [정올 185/Python] 문자열1 - 형성평가4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=85&sca=10e0

string, char = input().split()
for i in range(len(string)):
    if string[i] == char[0]:
        print(i)
        break
    elif i==(len(string)-1):
        print("No")
