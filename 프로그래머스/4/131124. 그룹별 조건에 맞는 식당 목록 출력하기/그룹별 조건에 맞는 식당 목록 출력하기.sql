SELECT M.member_name, R.review_text, DATE_FORMAT(R.review_date, '%Y-%m-%d') AS REVIEW_DATE
FROM member_profile M
JOIN rest_review R
ON M.member_id = R.member_id
WHERE R.member_id IN (
    SELECT member_id
    FROM rest_review
    GROUP BY member_id
    HAVING COUNT(*) = (
        SELECT MAX(cnt)
        FROM (
            SELECT member_id, COUNT(*) AS CNT
            FROM rest_review
            GROUP BY member_id
        ) T
    )
)
ORDER BY review_date, review_text;