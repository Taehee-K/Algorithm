# [정올 612/Python] 문자열2 - 자가진단B
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=249&sca=10f0

numbers = list(input().split()) # 5개의 정수 문자열로 입력받기
number = ""
for num in numbers:
    number+=num # 모두 붙여서 문자열로 저장
for i in range(len(number)//3+1):
    print(number[3*i:3*i+3])