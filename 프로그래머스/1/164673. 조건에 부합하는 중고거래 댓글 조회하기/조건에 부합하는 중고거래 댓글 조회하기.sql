SELECT used_goods_board.title, used_goods_board.board_id, used_goods_reply.reply_id, used_goods_reply.writer_id, used_goods_reply.contents, DATE_FORMAT(used_goods_reply.created_date, '%Y-%m-%d') AS created_date
FROM used_goods_board INNER JOIN used_goods_reply
ON used_goods_board.board_id = used_goods_reply.board_id
WHERE SUBSTR(used_goods_board.created_date, 1, 7) = '2022-10'
ORDER BY used_goods_reply.created_date, used_goods_board.title;
