-- Write your query below
select distinct c.title as title
from tv_program tv join content c on tv.content_id = c.content_id
where kids_content = 'Y'
and program_date::date between '2020-06-01' and '2020-06-30'
and content_type = 'Movies'