/**
자동차 종류가 '트럭'
대여 기록 별로 대여 금액(FEE)
*/

SELECT T.history_id,
    ROUND((
        CASE
            WHEN T.duration >= 7 AND T.duration < 30 THEN (T.daily_fee - (T.daily_fee * (
                SELECT CAST(REGEXP_REPLACE(discount_rate, '[^0-9]', '') AS UNSIGNED)
                FROM car_rental_company_discount_plan
                WHERE CAST(REGEXP_REPLACE(duration_type, '[^0-9]', '') AS UNSIGNED) = 7
                    AND car_type = '트럭'
            ) / 100)) * T.duration
            WHEN T.duration >= 30 AND T.duration < 90 THEN (T.daily_fee - (T.daily_fee * (
                SELECT CAST(REGEXP_REPLACE(discount_rate, '[^0-9]', '') AS UNSIGNED)
                FROM car_rental_company_discount_plan
                WHERE CAST(REGEXP_REPLACE(duration_type, '[^0-9]', '') AS UNSIGNED) = 30
                    AND car_type = '트럭'
            ) / 100)) * T.duration
            WHEN T.duration >= 90 THEN (T.daily_fee - (T.daily_fee * (
                SELECT CAST(REGEXP_REPLACE(discount_rate, '[^0-9]', '') AS UNSIGNED)
                FROM car_rental_company_discount_plan
                WHERE CAST(REGEXP_REPLACE(duration_type, '[^0-9]', '') AS UNSIGNED) = 90
                    AND car_type = '트럭'
            ) / 100)) * T.duration
            ELSE T.daily_fee * T.duration
        END
    ), 0) AS fee
FROM (
    SELECT C.car_id,
        C.daily_fee,
        R.history_id,
        DATEDIFF(R.end_date, R.start_date) + 1 AS duration
    FROM car_rental_company_car C
    JOIN car_rental_company_rental_history R
    ON C.car_id = R.car_id
    WHERE C.car_type = '트럭'
) T
ORDER BY fee DESC, T.history_id DESC