# [정올 598/Python] 문자열1 - 자가진단6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=235&sca=10e0

while True:
    char = input().strip() # strip() 함수로 뒤의 공백 제거
    if char.isalpha(): # isalpha()로 문자열인지 확인
        print(char)
    elif char.isdigit():    #isdigit()로 숫자인지 확인
        print(ord(char))    # ord() 함수로 ASCII 코드값 출력하기
    else:   # 문자/숫자가 아닐 때
        break   # 종료