SELECT A.food_type, A.rest_id, A.rest_name, A.favorites
FROM rest_info A
INNER JOIN (
    SELECT food_type, MAX(favorites) AS MAX_FAVORITES
    FROM rest_info
    GROUP BY food_type
) B
ON A.food_type LIKE B.food_type AND A.favorites = B.max_favorites
ORDER BY A.food_type DESC;