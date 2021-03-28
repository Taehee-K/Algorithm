# [정올 215/Python] 문자열2 - 형성평가7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=115&sca=10f0

def Number(string):
    num = ""
    for i in range(len(string)):
        if string[i].isnumeric():
            num+=string[i]
        else: break
    return int(num)
str1, str2 = input().split()
str1 = Number(str1)
str2 = Number(str2)
print(str1*str2)