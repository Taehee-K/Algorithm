-- [프로그래머스 Lv2/SQL] 중성화 여부 파악하기
-- https://programmers.co.kr/learn/courses/30/lessons/59409

SELECT ANIMAL_ID, NAME, 
    CASE 
    WHEN SEX_UPON_INTAKE IN ('Neutered Male', 'Spayed Female') THEN 'O'
    ELSE 'X'
    END AS '중성화'    -- END 지정해 주어야 함
FROM ANIMAL_INS
ORDER BY ANIMAL_ID