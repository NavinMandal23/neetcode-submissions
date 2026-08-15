-- Write your query below
with cte as (
    select name as customer_name, c.customer_id, order_id, order_date, rank() over(partition by c.customer_id order by order_date desc) rnk
    from customers c join orders o on c.customer_id = o.customer_id
)

select customer_name, customer_id, order_id, order_date
from cte 
where rnk <= 3
order by 1 asc, 2 asc, 4 desc