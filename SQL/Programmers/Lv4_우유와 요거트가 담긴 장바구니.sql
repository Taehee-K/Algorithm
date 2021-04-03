-- [프로그래머스 Lv4/SQL] 우유와 요거트가 담긴 장바구니
-- https://programmers.co.kr/learn/courses/30/lessons/62284

SELECT CART_ID                      -- CART_ID 조회
FROM CART_PRODUCTS              
WHERE NAME IN ('Milk', 'Yogurt')    -- 상품이 Milk 또는 Yogurt일 떄
GROUP BY CART_ID                    -- 장바구니 아이디별로 GROUP
HAVING COUNT(DISTINCT NAME)>= 2     -- 유일한 상품 2개 이상일 때

-- DISTINCT NAME 처음에 적용하지 않아서 틀림