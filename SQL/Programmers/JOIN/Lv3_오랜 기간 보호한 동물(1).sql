-- [프로그래머스 Lv3/SQL] 오랜 기간 보호한 동물(1)
-- https://programmers.co.kr/learn/courses/30/lessons/59044

SELECT INS.NAME, INS.DATETIME
FROM 
    ANIMAL_INS INS
        LEFT OUTER JOIN ANIMAL_OUTS OUTS
        ON INS.ANIMAL_ID = OUTS.ANIMAL_ID 
WHERE OUTS.ANIMAL_ID IS NULL    
ORDER BY INS.DATETIME
LIMIT 3 -- LIMIT 사용하여 상위 3개 출력

-- IS NULL 이 아닌 OUTS.ANIMAL_ID = NULL으로 해서 틀림