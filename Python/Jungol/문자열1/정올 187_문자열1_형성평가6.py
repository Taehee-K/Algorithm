# [정올 187/Python] 문자열1 - 형성평가6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=87&sca=10e0

string = input()
while len(string)>1:
    num = int(input()) # 제거할 문자의 위치(첫 번째 문자 위치 = 1)
    if num> len(string): # 입력받은 번호가 문자열의 길이 이상일 시
        string = string[:len(string)-1] # 마지막 문자 제거
    else:
        string = string[:num-1]+string[num:] # num 위치의 문자 제거
    print(string) 

