-- [프로그래머스 Lv2/SQL] DATETIME에서 DATE로 형 변환
-- https://programmers.co.kr/learn/courses/30/lessons/59414

SELECT ANIMAL_ID, NAME, date_format(DATETIME, '%Y-%m-%d')
FROM ANIMAL_INS

-- %Y-> yyyy, %y-> yy
-- %M-> January, Febuary... , %m-> 01, 02, ...
-- %D-> 1st, 2nd, ..., %d -> 01, 02, ...