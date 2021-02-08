-- [프로그래머스 코딩테스트/SQL] 없어진 기록 찾기
-- https://programmers.co.kr/learn/courses/30/lessons/59042


SELECT ANIMAL_ID, NAME 
FROM ANIMAL_OUTS OUTS
WHERE ANIMAL_ID NOT IN (SELECT INS.ANIMAL_ID
                        FROM ANIMAL_INS AS INS)
ORDER BY OUTS.ANIMAL_ID
