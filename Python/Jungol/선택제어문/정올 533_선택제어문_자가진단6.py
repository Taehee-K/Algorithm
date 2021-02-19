# [정올 533/Python] 선택제어문 - 자가진단6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=170&sca=1050
 
# 남자는 'M' 여자는 'F'
# 18세 이상은 성인


# 성별('M', 'F')과 나이를 입력
gender, age = input().split()
age = int(age)

# "MAN"(성인남자), "WOMAN"(성인여자), "BOY"(미성년남자), "GIRL"(미성년여자)을 구분하여 출력
if gender =='M':
    if age>=18: print("MAN")
    else: print("BOY")
elif gender =='F':
    if age>=18: print('WOMAN')
    else: print('GIRL')
