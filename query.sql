Select * from customer
LEFT JOIN address
on customer.id = address.customer_id