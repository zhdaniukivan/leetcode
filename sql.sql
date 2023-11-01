CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    Price DECIMAL(10, 2),
    Quantity INT
);

INSERT INTO Products (ProductID, ProductName, Price, Quantity)
VALUES
    (1, 'Товар 1', 10.99, 100),
    (2, 'Товар 2', 25.50, 50),
    (3, 'Товар 3', 5.99, 200);

SELECT * FROM Products
WHERE Price > 10.00;

UPDATE Products
SET Price = Price * 1.10;


CREATE TRIGGER IncreasePriceTrigger
BEFORE INSERT ON Products
FOR EACH ROW
BEGIN
    SET NEW.Price = NEW.Price * 1.10;
END;

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    ShipDate DATE,
    ShipMethod VARCHAR(50),
    TotalAmount DECIMAL(12, 2),
    Status VARCHAR(20)
);
INSERT INTO Orders (OrderID, CustomerID, OrderDate, ShipDate, ShipMethod, TotalAmount, Status)
VALUES
    (1, 101, '2023-10-01', '2023-10-03', 'Courier', 150.50, 'Shipped'),
    (2, 102, '2023-10-02', '2023-10-05', 'Express', 275.75, 'Delivered'),
    (3, 103, '2023-10-03', '2023-10-04', 'Standard', 85.25, 'Processing');

SELECT * FROM Orders
WHERE CustomerID = 101;

UPDATE Orders
SET Status = 'Shipped'
WHERE OrderID = 3;

CREATE TRIGGER IncreaseOrderTotalTrigger
BEFORE INSERT ON Orders
FOR EACH ROW
BEGIN
    SET NEW.TotalAmount = NEW.TotalAmount * 1.05;
END;

