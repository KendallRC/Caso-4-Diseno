-- init.sql

-- Seleccionar la base de datos
USE diseno;

-- Crear la tabla si no existe
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255)

);

-- Insertar datos aleatorios
DELIMITER //

CREATE PROCEDURE insert_random_records()
BEGIN
    DECLARE i INT DEFAULT 0;
    WHILE i < 10 DO
        INSERT INTO products (name, description) VALUES
        (CONCAT('producto ', @numero := FLOOR(RAND() * 10000)), CONCAT('descripcion del producto ', @numero));
        SET i = i + 1;
    END WHILE;
END //

DELIMITER ;

-- Llamar al procedimiento para insertar los registros
CALL insert_random_records();

-- Eliminar el procedimiento si ya no es necesario
DROP PROCEDURE insert_random_records;
