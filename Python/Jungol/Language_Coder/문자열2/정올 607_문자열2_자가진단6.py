# [정올 607/Python] 문자열2 - 자가진단6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=244&sca=10f0

word1, word2 = input().split()
word2 = word1[:2]+word2[2:]+word1[:2] 
print(word2)
