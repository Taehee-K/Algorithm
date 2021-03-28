# [정올 182/Python] 문자열1 - 형성평가1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=82&sca=10e0

chr1, chr2 = input().split() # 영문자 2개 입력 
# ord() 함수 이용해 영문자 -> ASCII 코드값 변환
print(ord(chr1)+ord(chr2), end = " ") # ASCII 코드의 합 출력
print(abs(ord(chr1)-ord(chr2))) # ASCII 코드의 차 출력