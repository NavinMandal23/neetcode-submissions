-- Write your query below
SELECT seller_name
FROM seller where not exists (select 1 from orders where
extract(year from sale_date) = '2020' and seller.seller_id = orders.seller_id)
order by seller_name asc