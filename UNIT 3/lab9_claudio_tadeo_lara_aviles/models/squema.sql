CREATE DATABASE IF NOT EXISTS lab8_login;
USE lab8_login;
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    password VARCHAR(10) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);

INSERT INTO users (nombre, password, email) VALUES
('admin', 'admin!123', 'chase@gmail.com');

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);

INSERT INTO products (nombre, precio) VALUES
('Laptop HP Pavilion', 14500.00),
('Mouse Inalámbrico Logitech', 450.50),
('Teclado Mecánico RGB', 1200.00),
('Monitor LED 24 pulgadas', 3100.00),
('Audífonos Diadema Gamer', 850.00);