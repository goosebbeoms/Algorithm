SELECT II.item_id, II.item_name
FROM item_info II
RIGHT JOIN (
    SELECT *
    FROM item_tree
    WHERE parent_item_id IS NULL
) IT
ON II.item_id = IT.item_id
ORDER BY II.item_id;