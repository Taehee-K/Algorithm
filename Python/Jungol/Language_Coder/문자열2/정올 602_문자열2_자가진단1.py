# [정올 602/Python] 문자열2 - 자가진단1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=239&sca=10f0

words = [input() for _ in range(5)] # 5개의 단어 입력받기
for i in range(4, -1, -1): # 역순으로 출력
    print(words[i])