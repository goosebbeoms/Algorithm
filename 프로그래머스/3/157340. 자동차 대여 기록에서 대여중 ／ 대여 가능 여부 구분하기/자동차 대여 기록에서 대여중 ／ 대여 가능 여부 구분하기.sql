SELECT A.car_id,
    IF(B.checker IS NOT NULL, '대여중', '대여 가능') AS availability
FROM (
    SELECT DISTINCT car_id
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
) A
LEFT JOIN (
    SELECT *
    FROM (
        SELECT car_id,
            IF('2022-10-16' BETWEEN start_date AND end_date, '대여중', NULL) AS checker
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    ) A
    WHERE checker IS NOT NULL
) B
ON A.car_id = B.car_id
ORDER BY A.car_id DESC;