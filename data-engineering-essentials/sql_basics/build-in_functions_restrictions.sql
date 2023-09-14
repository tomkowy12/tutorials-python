SELECT * FROM orders;

SELECT order_status, count(*) AS order_count
FROM orders
GROUP BY 1
ORDER BY 2 DESC;

SELECT order_date, count(*) AS order_count
FROM orders
GROUP BY 1
ORDER BY 2 DESC;

SELECT to_char(order_date, 'yyyy-MM') AS order_month, count(*) AS order_count
FROM orders
GROUP BY 1
ORDER BY 2 DESC;

SELECT order_item_order_id, round(sum(order_item_subtotal)::numeric, 2) AS order_revenue 
FROM order_items
GROUP BY 1
ORDER BY 2;

SELECT order_item_order_id, round(sum(order_item_subtotal)::numeric, 2) AS order_revenue 
FROM order_items
-- wrong: WHERE order_revenue > 15, we do not use such a composition
GROUP BY 1
ORDER BY order_revenue;

-- This is the order of executing:
-- SELECT, FROM, WHERE -- prepare data
-- GROUP BY -- group prepared data, so prepare new dataset
-- ORDER BY -- change data order

