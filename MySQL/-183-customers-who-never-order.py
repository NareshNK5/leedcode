'''
# Write your MySQL query statement below
SELECT name as Customers
from Customers
LEFT JOIN Orders
ON Customers.id=Orders.customerID
where Orders.customerID IS Null


select c.name as Customers
from customers c
where not exists (select o.id
                from orders o
                where o.customerId = c.id)

'''