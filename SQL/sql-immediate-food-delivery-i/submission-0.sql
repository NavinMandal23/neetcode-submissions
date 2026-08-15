-- Write your query below
select round(count(case when order_date = customer_pref_delivery_date then delivery_id end)*100.0 / count(delivery_id), 2) as immediate_percentage
from delivery