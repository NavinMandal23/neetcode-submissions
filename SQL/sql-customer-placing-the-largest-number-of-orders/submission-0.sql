SELECT customer_number FROM
(SELECT customer_number, count(order_number) cnt FROM orders
GROUP BY 1 ) s
ORDER BY cnt DESC LIMIT 1 