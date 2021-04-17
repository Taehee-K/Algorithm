# [코드업 6074/Python] 반복실행구조 - 문자 1개 입력받아 알파벳 출력하기
# https://codeup.kr/problem.php?id=6074

c = ord(input())    # 문자 입력받아 ASCII 코드값으로 변환
letter = ord('a')   

while letter<=c:
    print(chr(letter), end = " ")
    letter+=1