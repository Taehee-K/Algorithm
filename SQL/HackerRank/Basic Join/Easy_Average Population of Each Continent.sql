-- [HackerRank Easy/SQL] Average Population of Each Continent
-- https://www.hackerrank.com/challenges/average-population-of-each-continent/problem

SELECT COUNTRY.CONTINENT, FLOOR(SUM(CITY.POPULATION)/COUNT(CITY.ID))
FROM COUNTRY, CITY
WHERE COUNTRY.CODE = CITY.COUNTRYCODE
GROUP BY COUNTRY.CONTINENT
