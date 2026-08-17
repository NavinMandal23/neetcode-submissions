-- Write your query below
with cte as (
    select transaction_id, rank() over(partition by day::date order by amount desc) rnk
    from transactions
)

select transaction_id 
from cte 
where rnk = 1
order by 1 
