# [정올 611/Python] 문자열2 - 자가진단A
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=248&sca=10f0

string = input()
number = ""
for i in range(len(string)):
    if string[i].isdigit():
        number+=string[i]
    elif string[i]=="." and '.' not in number:
        number+=string[i]
    else: break
print(int(float(number))*2)
print("{:.2f}".format(float(number)))