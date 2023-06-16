SELECT * FROM Customers WHERE Country = "France";
SELECT * FROM Customers WHERE Country = "France" OR Country = "Mexico";
SELECT City FROM Customers WHERE City LIKE 'L%';
SELECT CustomerName, CustomerID, Country FROM Customers WHERE Address LIKE '%Berg%'
SELECT ContactName, Address, City, Country, PostalCode FROM Customers WHERE CustomerName LIKE '%Antonio%'