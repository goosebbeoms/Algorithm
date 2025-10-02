-- 코드를 입력하세요
SELECT CONCAT('/home/grep/src/', B.board_id, '/', F.file_id, F.file_name, F.file_ext) AS FILE_PATH
FROM used_goods_board B
INNER JOIN used_goods_file F
ON B.board_id = F.board_id
WHERE B.views = (
    SELECT views
    FROM used_goods_board
    ORDER BY views DESC
    LIMIT 1
)
ORDER BY F.file_id DESC