SELECT II.item_id, II.item_name, II.rarity
FROM item_info II
LEFT JOIN (
    SELECT DISTINCT parent_item_id
    FROM item_tree
) IT
ON II.item_id = IT.parent_item_id
WHERE IT.parent_item_id IS NULL
ORDER BY II.item_id DESC;