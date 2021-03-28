# [정올 599/Python] 문자열1 - 자가진단7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=236&sca=10e0

string = input()
for i in range(len(string)): # 문자열의 길이만큼 반복
    if string[i].isalpha(): # isalpha() 함수 사용해 알파벳인지 확인
        print(string[i].upper(), end = "") # upper() 함수로 대문자 출력
    else: continue