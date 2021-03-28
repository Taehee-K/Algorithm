# [정올 593/Python] 문자열1 - 자가진단1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=230&sca=10e0

while True:
    n = int(input("ASCII code =? ")) 
    if n>=33 and n<=127: # 33~127 범위 이내의 숫자일 때
        print(chr(n))   # chr() 통해 문자 -> ASCII 코드값
                        # ord() 통해 ASCII 코드값 -> 문자
    else: # 해당 범위의 숫자가 아닐 때
        break # 종료
    

