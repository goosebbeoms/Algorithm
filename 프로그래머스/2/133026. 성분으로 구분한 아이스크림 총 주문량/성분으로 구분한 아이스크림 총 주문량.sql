SELECT icecream_info.ingredient_type AS INGREDIENTTYPE,
    SUM(first_half.total_order) AS TOTALORDER
FROM first_half
INNER JOIN icecream_info
ON first_half.flavor LIKE icecream_info.flavor
GROUP BY icecream_info.ingredient_type
ORDER BY totalorder ASC;