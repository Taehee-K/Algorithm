# [정올 610/Python] 문자열2 - 자가진단9
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=247&sca=10f0

words = [input() for _ in range(5)] # 5개의 문자열 입력
words.sort(reverse = True) # 역순으로 정렬
for word in words:
    print(word)