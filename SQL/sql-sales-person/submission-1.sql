-- Write your query below
with cte as (
    select 
    o.sales_id
    from orders o join company c on o.com_id = c.com_id
    where c.name = 'CRIMSON'
)

select name from sales_person p where not exists (select sales_id from cte c where c.sales_id = p.sales_id)