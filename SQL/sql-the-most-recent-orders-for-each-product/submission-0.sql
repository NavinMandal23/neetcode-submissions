-- Write your query below
with ranked as (
    select p.product_name, p.product_id, o.order_id, o.order_date, rank() over(partition by p.product_id order by o.order_date desc) rnk
    from orders o 
    -- join customers c on o.customer_id = c.customer_id
    join products p on p.product_id = o.product_id
)


select product_name, product_id, order_id, order_date
from ranked where rnk = 1
order by 1 asc, 2 asc, 3 asc