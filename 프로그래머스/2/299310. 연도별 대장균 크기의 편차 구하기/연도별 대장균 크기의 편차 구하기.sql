SELECT YEAR(A.differentiation_date) AS YEAR,
    ABS(B.max_size - A.size_of_colony) AS YEAR_DEV,
    A.id
FROM ecoli_data A
LEFT JOIN (
    SELECT YEAR(differentiation_date) AS 'YEAR',
        MAX(size_of_colony) AS 'MAX_SIZE'
    FROM ecoli_data
    GROUP BY YEAR(differentiation_date)
) B
ON YEAR(A.differentiation_date) = B.year
ORDER BY YEAR, YEAR_DEV;
