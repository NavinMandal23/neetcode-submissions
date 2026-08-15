-- Write your query below
with cte as (
    select sale_date, 
    sum(case when fruit = 'apples' then sold_num end) as n_apples,
    sum(case when fruit = 'oranges' then sold_num end) as n_oranges
    from sales
    group by 1
)
select sale_date, n_apples - n_oranges as diff
from cte 
order by 1