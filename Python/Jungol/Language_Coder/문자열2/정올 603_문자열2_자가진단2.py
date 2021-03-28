# [정올 603/Python] 문자열2 - 자가진단2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=240&sca=10f0

words = list(input().split()) # 문장 공백 단위로 저장
for i in range(len(words)):
    if i%2==0: # 홀수 번째 단어들 출력
        print(words[i]) 