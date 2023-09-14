SELECT DISTINCT order_status FROM orders
ORDER BY 1;

SELECT * FROM orders
WHERE order_status = 'COMPLETE'

SELECT * FROM orders
WHERE order_status = 'ClOSED'

SELECT * FROM orders
WHERE order_status = 'CLOSED' OR order_status = 'COMPLETE';

SELECT * FROM orders
WHERE order_status IN ('CLOSED', 'COMPLETE');

SELECT count(*) FROM orders;

SELECT count(*) FROM order_items;

SELECT count(DISTINCT order_status) FROM orders;

SELECT count(DISTINCT order_date) FROM orders;

SELECT * FROM order_items WHERE order_item_order_id = 2;;

SELECT sum(order_item_subtotal) 
FROM order_items
WHERE order_item_order_id = 2;

SELECT * FROM orders;

