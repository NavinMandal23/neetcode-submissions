-- Write your query below
WITH cte AS (
    SELECT c.customer_id, c.customer_name,
    count(distinct case when product_name = 'A' then order_id end) cnt_A,
    count(distinct case when product_name = 'B' then order_id end) cnt_B,
    count(distinct case when product_name = 'C' then order_id end) cnt_C
    FROM customers c JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY 1, 2
)
SELECT customer_id, customer_name
FROM cte 
WHERE cnt_a > 0 AND cnt_b > 0 and cnt_c = 0
ORDER BY 2 
