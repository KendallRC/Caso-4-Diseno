-- init.sql

-- Seleccionar la base de datos
USE diseño;

-- Crear la tabla si no existe
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    column1 VARCHAR(255),
    column2 INT
);

-- Insertar datos aleatorios
DELIMITER //

CREATE PROCEDURE insert_random_records()
BEGIN
    DECLARE i INT DEFAULT 0;
    WHILE i < 6000 DO
        INSERT INTO products (column1, column2) VALUES
        (CONCAT('random_text_', FLOOR(RAND() * 10000)), FLOOR(RAND() * 10000));
        SET i = i + 1;
    END WHILE;
END //

DELIMITER ;

-- Llamar al procedimiento para insertar los registros
CALL insert_random_records();

-- Eliminar el procedimiento si ya no es necesario
DROP PROCEDURE insert_random_records;
