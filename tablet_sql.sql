-- Таблица "Authors" (Авторы)
CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY,
    AuthorName VARCHAR(255),
    Biography TEXT,
    YearsOfLife VARCHAR(20)
);

-- Таблица "Genres" (Жанры)
CREATE TABLE Genres (
    GenreID INT PRIMARY KEY,
    GenreName VARCHAR(50)
);

-- Таблица "Books" (Книги)
CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(255),
    AuthorID INT,
    GenreID INT,
    Price DECIMAL(10, 2),
    Quantity INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID),
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID)
);

-- Вставка данных в таблицу "Authors"
INSERT INTO Authors (AuthorID, AuthorName, Biography, YearsOfLife)
VALUES
    (1, 'Лев Толстой', 'Русский писатель...', '1828-1910'),
    (2, 'Джейн Остин', 'Английская писательница...', '1775-1817'),
    (3, 'Федор Достоевский', 'Русский писатель...', '1821-1881');


-- Вставка данных в таблицу "Genres"
INSERT INTO Genres (GenreID, GenreName)
VALUES
    (1, 'Роман'),
    (2, 'Детектив'),
    (3, 'Фантастика');

-- Вставка данных в таблицу "Books"
INSERT INTO Books (BookID, Title, AuthorID, GenreID, Price, Quantity)
VALUES
    (1, 'Война и мир', 1, 1, 25.99, 100),
    (2, 'Гордость и предубеждение', 2, 1, 19.99, 75),
    (3, 'Преступление и наказание', 3, 2, 15.50, 120),
    (4, 'Анна Каренина', 1, 1, 22.75, 80),
    (5, 'Идиот', 3, 1, 18.99, 90);

SELECT b.Title, a.AuthorName
FROM Books b
JOIN Authors a ON b.AuthorID = a.AuthorID
WHERE a.AuthorName = 'Лев Толстой';

SELECT b.Title, g.GenreName
FROM Books b
JOIN Genres g ON b.GenreID = g.GenreID
WHERE g.GenreName = 'Роман';

SELECT AVG(Price) AS AveragePrice
FROM Books;