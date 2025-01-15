WITH RECURSIVE number_sequence AS (
    SELECT 0 AS 'HOUR'
    UNION
    SELECT hour + 1
    FROM number_sequence
    WHERE hour < 23
)

SELECT number_sequence.hour,
    IF(cal_table.count IS NOT NULL, cal_table.count, 0) AS 'COUNT'
FROM (
    SELECT HOUR(datetime) AS 'HOUR', COUNT(*) AS 'COUNT'
    FROM animal_outs
    GROUP BY HOUR(datetime)
) cal_table
RIGHT JOIN number_sequence
ON number_sequence.hour = cal_table.hour;