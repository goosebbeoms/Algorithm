-- 조건1: 자동차가 '세단' 또는 'SUV'
-- 조건2: 2022년 11월 1일 ~ 2022년 11월 30일 대여 가능
-- 조건3: 30일 간의 대여 금액이 50만원 이상 200만원 미만
-- 정렬: 대여 금액 기준 DESC, 자동차 종류 기준 ASC, 자동차 ID 기준 DESC

SELECT C.car_id, C.car_type, FLOOR(C.daily_fee * 30 * (100 - D.discount_rate) / 100) AS fee
FROM car_rental_company_car C
JOIN car_rental_company_discount_plan D
ON D.car_type = C.car_type AND D.duration_type = '30일 이상'
WHERE C.car_type IN ('세단', 'SUV')
    AND NOT EXISTS (
        SELECT 1
        FROM car_rental_company_rental_history H
        WHERE H.car_id = C.car_id
            AND H.start_date <= TO_DATE('2022-11-30', 'YYYY-MM-DD')
            AND H.end_date >= TO_DATE('2022-11-01', 'YYYY-MM-DD')
    )
    AND FLOOR(C.daily_fee * 30 * (100 - D.discount_rate) / 100) >= 500000
    AND FLOOR(C.daily_fee * 30 * (100 - D.discount_rate) / 100) < 2000000
ORDER BY fee DESC, C.car_type ASC, C.car_id DESC;