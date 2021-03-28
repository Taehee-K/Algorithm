# [정올 192/Python] 문자열2 - 형성평가4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=92&sca=10f0

n = int(input())
words = [input().strip() for _ in range(n)] # n개의 문자열 입력
words.sort() # 오름차순 정렬
for word in words:
    print(word)