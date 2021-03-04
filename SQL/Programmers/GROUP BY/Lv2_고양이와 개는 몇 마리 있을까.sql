-- [프로그래머스 Lv2/SQL] 고양이와 개는 몇 마리 있을까
-- https://programmers.co.kr/learn/courses/30/lessons/59040

SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) as count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE 
ORDER BY ANIMAL_TYPE --고양이를 개보다 먼저 조회

