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
    DECLARE i INT DEFAULT 1;  -- Declarar i como variable local e inicializar en 1
    WHILE i <= 59999 DO  -- Cambiar < 10 a <= 10 para incluir el número 10
        INSERT INTO products (name, description) VALUES
        (CONCAT('producto ', i), CONCAT('descripcion del producto ', i));
        SET i = i + 1;  -- Incrementar el contador
    END WHILE;
END //

DELIMITER ;

-- Llamar al procedimiento para insertar los registros
CALL insert_random_records();

-- Eliminar el procedimiento si ya no es necesario
DROP PROCEDURE insert_random_records;
