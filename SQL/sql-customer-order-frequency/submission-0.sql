-- Write your query below
with cte as (
    select 
        to_char(o.order_date, 'YYYY-MM') as year_month,
        c.customer_id, 
        c.name,
        sum(p.price * o.quantity) as amount
    from customers c
    join orders o on c.customer_id = o.customer_id
    join product p on o.product_id = p.product_id
    where o.order_date between '2020-06-01' and '2020-07-31'
    group by 1,2,3
)

select customer_id, name 
from cte
where amount >= 100 and year_month IN ('2020-06', '2020-07')
group by 1,2 
having count(1) = 2