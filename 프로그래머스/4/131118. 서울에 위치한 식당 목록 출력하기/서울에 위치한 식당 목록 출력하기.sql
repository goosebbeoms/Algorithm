SELECT rest_info.rest_id, rest_name, food_type, favorites, address, ROUND(AVG(review_score), 2) AS score
FROM rest_info inner join rest_review
    on rest_info.rest_id = rest_review.rest_id
WHERE rest_info.address like '서울%'
GROUP BY rest_info.rest_id
ORDER BY AVG(review_score) DESC, favorites DESC;