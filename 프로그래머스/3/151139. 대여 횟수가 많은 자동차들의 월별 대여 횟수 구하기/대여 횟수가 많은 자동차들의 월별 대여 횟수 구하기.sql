SELECT MONTH(default_table.start_date) AS 'MONTH',
    default_table.car_id AS 'CAR_ID',
    COUNT(*) AS 'RECORDS'
FROM (
    SELECT *
    FROM car_rental_company_rental_history
    WHERE 1 = 1
        AND (YEAR(start_date) = 2022 AND MONTH(start_date) in (8, 9, 10))
        # AND (YEAR(end_date) = 2022 AND MONTH(end_date) in (8, 9, 10))
) default_table
INNER JOIN (
    SELECT car_id
    FROM car_rental_company_rental_history
    WHERE 1 = 1
        AND (YEAR(start_date) = 2022 AND MONTH(start_date) in (8, 9, 10))
        # OR (YEAR(end_date) = 2022 AND MONTH(end_date) in (8, 9, 10))
    GROUP BY car_id
    HAVING COUNT(*) >= 5
) car_id_table
ON default_table.car_id = car_id_table.car_id
GROUP BY MONTH(default_table.start_date), default_table.car_id
ORDER BY month ASC, car_id DESC;