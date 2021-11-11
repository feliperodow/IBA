--We would like to report on the number of installations
--that the company is doing every month in order to see if the business is growing.

with num_installations as (
    select
        extract(year from installation_date) "Year",
        extract(month from installation_date) "Month",
        count(*)
    from
        installation
    group by
        extract(year from installation_date),
        extract(month from installation_date)
    order by 1, 2
)

select * from num_installations