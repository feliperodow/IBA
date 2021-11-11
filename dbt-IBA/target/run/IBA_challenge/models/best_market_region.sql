
  create view "awesomeinc"."public"."best_market_region__dbt_tmp" as (
    --Which region of the world is our best market.

with customer_expenses as(
	select cu.id, sum(cast(p.price as float)) as expenses
	from customer as cu, installation as ins, product as p
	where cu.id = ins.customer_id and p.id = ins.product_id
	group by cu.id
),

country_expenses as (
	select cu.country_id, sum(ce.expenses) as expenses
	from customer as cu, customer_expenses as ce
	where cu.id = ce.id
	group by cu.country_id
),

region_expenses as (
	select co.region, sum(ce.expenses) as expenses
	from country as co, country_expenses as ce
	where co.id = ce.country_id
	group by co.region
),

best_region as (
	select region, expenses
	from region_expenses
	where expenses = (select max(expenses) from region_expenses)
)

select * from best_region
  );
