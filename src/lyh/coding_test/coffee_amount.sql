-- 프로그래머스
-- https://programmers.co.kr/app/with_setting/tests/47122/challenges/sqls/987

SELECT a.coffee_id, b.name, sum(a.amount) amount
    FROM toss_coffee_log a
        INNER JOIN (
            SELECT id, name
            FROM toss_coffee
        ) b ON (a.coffee_id = b.id)
WHERE DATE(date) <= '2021-05-02'
GROUP BY a.coffee_id
ORDER BY b.id ASC;