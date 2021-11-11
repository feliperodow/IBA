--We would also like to see which product category brings us more revenues

with product_info as (
	select p.id, pc.name as prod_cat_name, p.reference, p.name as prod_name, p.price
	from product_category as pc, product as p
	where p.category_id = pc.id
	order by cast(p.price as float) asc
),

installations_per_product as (
	select product_id, count(product_id) as sells
	from installation
	group by product_id
),

total_sells_per_product as (
	select pi.prod_cat_name, ipp.sells, pi.price, ipp.sells*cast(pi.price as float) as revenue
	from product_info as pi, installations_per_product as ipp
	where pi.id = ipp.product_id
),

best_product_category_revenue as (
	select prod_cat_name, revenue
	from total_sells_per_product
	where revenue = (select max(revenue) from total_sells_per_product)
)

select * from best_product_category_revenue



