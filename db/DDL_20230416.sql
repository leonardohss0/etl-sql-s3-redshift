-- CREATE TABLE IN POSTGRESS

create table if not exists public.all_orders(
	order_id character varying,
	date date,
	product_name varchar(255),
	quantity integer,
	primary key (order_id)
)