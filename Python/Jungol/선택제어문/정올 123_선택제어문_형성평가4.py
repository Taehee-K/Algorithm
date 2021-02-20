# [정올 123/Python] 선택제어문 - 형성평가4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=23&sca=1050
 
# 1번은 개, 2번은 고양이, 3번은 병아리로
# 번호를 입력하면 번호에 해당하는 동물을 영어로 출력
# 해당 번호가 없으면 "I don't know."출력

# 개-dog, 고양이-cat, 병아리-chick​ 

num = int(input("Number? "))

if num==1: print("dog")
elif num==2: print("cat")
elif num==3: print("chick")
else: print("I don't know.")