# [정올 188/Python] 문자열1 - 형성평가7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=88&sca=10e0

string = list(input().split()) # 공백 기준으로 분리해 list에 저장
for i in range(len(string)):
    print(str(i+1)+". "+string[i])