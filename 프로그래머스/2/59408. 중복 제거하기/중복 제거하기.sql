SELECT COUNT(*) AS count
FROM(
    SELECT DISTINCT name
    FROM animal_ins
    WHERE name IS NOT NULL
) filtered;