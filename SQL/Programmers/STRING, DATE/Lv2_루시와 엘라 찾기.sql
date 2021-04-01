-- [프로그래머스 Lv2/SQL] 루시와 엘라 찾기
-- https://programmers.co.kr/learn/courses/30/lessons/59046

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID