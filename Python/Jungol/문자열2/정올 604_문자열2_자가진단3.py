# [정올 604/Python] 문자열2 - 자가진단3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=241&sca=10f0

words = [input().strip() for _ in range(10)] # 10개의 단어 입력받기
char = input().strip() # 한 개의 문자 입력받기
for i in range(len(words)): # 단어 개수만큼 반복
    if words[i][-1] == char[0]: # 단어의 마지막 문자 확인
        print(words[i]) 