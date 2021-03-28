# [정올 189/Python] 문자열2 - 형성평가1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=89&sca=10f0

words = list(input().split()) # 공백 기준 단어로 분리해 저장
for i in range(len(words)-1, -1, -1): # 입력 순서와 반대로 출력
    print(words[i])