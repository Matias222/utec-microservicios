DROP DATABASE IF EXISTS gestionpedidos;

-- Crear la base de datos si no existe
CREATE DATABASE gestionpedidos;

-- Usar la base de datos recién creada
USE gestionpedidos;

-- Crear la tabla clientes
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    telefono VARCHAR(20)
);

-- Crear la tabla pedidos
CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    fecha DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE CASCADE
);

-- Crear la tabla detalle_pedidos
CREATE TABLE detalle_pedidos (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_libro INT NOT NULL,  -- Relacionado con la tabla libros en MySQL
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido) ON DELETE CASCADE
);

-- Insertar valores de prueba en la tabla clientes
INSERT INTO clientes (nombre, correo, telefono) VALUES
('Cliente 1', 'cliente1@example.com', '1234567890'),
('Cliente 2', 'cliente2@example.com', '1234567891'),
('Cliente 3', 'cliente3@example.com', '1234567892'),
('Cliente 4', 'cliente4@example.com', '1234567893'),
('Cliente 5', 'cliente5@example.com', '1234567894'),
('Cliente 6', 'cliente6@example.com', '1234567895'),
('Cliente 7', 'cliente7@example.com', '1234567896'),
('Cliente 8', 'cliente8@example.com', '1234567897'),
('Cliente 9', 'cliente9@example.com', '1234567898'),
('Cliente 10', 'cliente10@example.com', '1234567899');

-- Insertar valores de prueba en la tabla pedidos
INSERT INTO pedidos (id_cliente, fecha, total) VALUES
(1, '2023-01-01', 59.99),
(2, '2023-01-02', 79.50),
(3, '2023-01-03', 35.20),
(4, '2023-01-04', 42.00),
(5, '2023-01-05', 99.99),
(6, '2023-01-06', 15.50),
(7, '2023-01-07', 120.00),
(8, '2023-01-08', 75.30),
(9, '2023-01-09', 85.60),
(10, '2023-01-10', 95.40);

-- Insertar valores de prueba en la tabla detalle_pedidos
INSERT INTO detalle_pedidos (id_pedido, id_libro, cantidad, precio_unitario) VALUES
(1, 1, 2, 25.99),
(2, 2, 1, 30.50),
(3, 3, 1, 15.00),
(4, 4, 3, 45.20),
(5, 5, 1, 20.00),
(6, 1, 1, 50.75),
(7, 3, 2, 10.99),
(8, 2, 1, 60.00),
(9, 5, 1, 35.40),
(10, 4, 2, 40.00);
