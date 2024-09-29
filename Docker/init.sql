USE diseno;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255)

);

-- Insertar datos aleatorios
DELIMITER //

CREATE PROCEDURE insert_random_records()
BEGIN
    DECLARE i INT DEFAULT 1;  
    WHILE i <= 59999 DO 
        INSERT INTO products (name, description) VALUES
        (CONCAT('producto ', i), CONCAT('descripcion del producto ', i));
        SET i = i + 1;  
    END WHILE;
END //

DELIMITER ;

CALL insert_random_records();

DROP PROCEDURE insert_random_records;
