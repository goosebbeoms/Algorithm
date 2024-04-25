SELECT COUNT(*) AS 'COUNT'
FROM ecoli_data
WHERE ((1 & genotype) or (4 & genotype)) and (not(2 & genotype));