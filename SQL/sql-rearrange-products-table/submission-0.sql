-- Write your query below
with cte as (
select 
    product_id, 
    unnest(ARRAY['store1', 'store2', 'store3']) as store,
    unnest(ARRAY[store1, store2, store3]) as price
from products
)
select * from cte
where price is not null