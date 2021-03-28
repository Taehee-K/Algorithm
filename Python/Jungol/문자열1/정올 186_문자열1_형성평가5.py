# [정올 186/Python] 문자열1 - 형성평가5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=86&sca=10e0

word1, word2 = input().split()
# word1의 길이가 더 길도록 만들어준다
if len(word1)<len(word2): word1, word2 = word2, word1 
print(len(word1))