# [정올 216/Python] 문자열2 - 형성평가8
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=116&sca=10f0

while True:
    word = input().strip()
    if word=='END': break
    else:
        print(word[::-1]) # 단어 뒤집어 출력