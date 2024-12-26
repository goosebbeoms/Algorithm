WITH RECURSIVE recur AS (
    SELECT id, parent_id, 1 AS generation
    FROM ecoli_data
    WHERE 1 = 1 AND parent_id IS NULL
    
    UNION ALL
    
    -- 재귀 쿼리
    SELECT ED.id, ED.parent_id, recur.generation+1 AS generation
    FROM ecoli_data ED
    INNER JOIN recur
    ON ED.parent_id = recur.id
)
SELECT COUNT(*) AS 'COUNT', generation
FROM recur
WHERE 1 = 1 AND id NOT IN (
    SELECT parent_id
    FROM recur
    WHERE parent_id IS NOT NULL
)
GROUP BY generation
ORDER BY generation;