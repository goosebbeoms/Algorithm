SELECT F.flavor
FROM (
    SELECT J.flavor, SUM(J.total_order) + FH.total_order AS calc
    FROM first_half FH
    RIGHT JOIN july J
    ON FH.flavor = J.flavor
    GROUP BY J.flavor
    ORDER BY calc DESC
) F
LIMIT 3;
