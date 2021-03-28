# [정올 184/Python] 문자열1 - 형성평가3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=84&sca=10e0

string = input()
for i in range(len(string)): # 문자열 길이만큼 반복
    if string[i].isalpha(): # 해당 자리의 문자가 영문자일 때
        print(string[i].lower(), end = "") # lower() 함수 -> 소문자 출력
    elif string[i].isdigit(): # 해당 자리의 문자가 숫자일 때
        print(string[i], end = "")
    else: continue